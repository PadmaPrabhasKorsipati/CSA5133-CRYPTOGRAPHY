import customtkinter as ctk
import threading
import queue

from voice_client import VoiceClient
from gui import VoiceMessengerGUI


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoginWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Secure Voice Messenger")
        self.geometry("450x500")
        self.resizable(False, False)

        self.client = None
        self.dashboard = None

        # Queue for communication between
        # background threads and Tkinter main thread
        self.gui_queue = queue.Queue()

        self.build()

        # Start GUI event processor
        self.after(
            50,
            self.process_gui_events
        )

    # =========================================================
    # BUILD LOGIN GUI
    # =========================================================

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="🔒 Secure Voice Messenger",
            font=("Arial", 26, "bold")
        )

        title.pack(pady=40)

        # -----------------------------------------------------
        # Username
        # -----------------------------------------------------

        self.username = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Username (Alice/Bob)"
        )

        self.username.pack(pady=15)

        # -----------------------------------------------------
        # Relay IP
        # -----------------------------------------------------

        self.host = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Relay IP"
        )

        self.host.insert(
            0,
            "127.0.0.1"
        )

        self.host.pack(pady=15)

        # -----------------------------------------------------
        # Port
        # -----------------------------------------------------

        self.port = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Port"
        )

        self.port.insert(
            0,
            "5000"
        )

        self.port.pack(pady=15)

        # -----------------------------------------------------
        # Connect Button
        # -----------------------------------------------------

        self.connect_btn = ctk.CTkButton(
            self,
            text="Connect",
            width=220,
            height=45,
            command=self.connect
        )

        self.connect_btn.pack(pady=40)

        # -----------------------------------------------------
        # Status
        # -----------------------------------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Not Connected",
            text_color="orange"
        )

        self.status.pack()

    # =========================================================
    # GUI QUEUE PROCESSOR
    # =========================================================

    def process_gui_events(self):

        try:

            while True:

                event, data = self.gui_queue.get_nowait()

                # ---------------------------------------------
                # Connected
                # ---------------------------------------------

                if event == "connected":

                    self._update_connected()

                # ---------------------------------------------
                # Secure channel
                # ---------------------------------------------

                elif event == "secure":

                    self.open_dashboard()

                # ---------------------------------------------
                # Connection error
                # ---------------------------------------------

                elif event == "error":

                    self.connection_failed(
                        data
                    )

        except queue.Empty:

            pass

        # Check again after 50 ms
        self.after(
            50,
            self.process_gui_events
        )

    # =========================================================
    # CONNECT
    # =========================================================

    def connect(self):

        username = self.username.get().strip()

        # -----------------------------------------------------
        # Validate username
        # -----------------------------------------------------

        if not username:

            self.status.configure(
                text="Please enter username",
                text_color="red"
            )

            return

        # -----------------------------------------------------
        # Only Alice / Bob
        # -----------------------------------------------------

        if username.lower() not in ["alice", "bob"]:

            self.status.configure(
                text="Username must be Alice or Bob",
                text_color="red"
            )

            return

        # -----------------------------------------------------
        # Validate port
        # -----------------------------------------------------

        port_text = self.port.get().strip()

        try:

            int(port_text)

        except ValueError:

            self.status.configure(
                text="Invalid port number",
                text_color="red"
            )

            return

        # -----------------------------------------------------
        # Update GUI
        # -----------------------------------------------------

        self.status.configure(
            text="Connecting...",
            text_color="yellow"
        )

        self.connect_btn.configure(
            state="disabled"
        )

        self.username.configure(
            state="disabled"
        )

        self.host.configure(
            state="disabled"
        )

        self.port.configure(
            state="disabled"
        )

        # -----------------------------------------------------
        # Create Voice Client
        # -----------------------------------------------------

        self.client = VoiceClient()

        # -----------------------------------------------------
        # Callback: Connected
        # -----------------------------------------------------

        self.client.on_connected = self.client_connected

        # -----------------------------------------------------
        # Callback: Secure
        # -----------------------------------------------------

        self.client.on_secure = self.secure_channel_ready

        # -----------------------------------------------------
        # Start Voice Client in background thread
        # -----------------------------------------------------

        threading.Thread(
            target=self.start_client,
            args=(username,),
            daemon=True
        ).start()

    # =========================================================
    # START CLIENT
    # =========================================================

    def start_client(self, username):

        try:

            self.client.start(
                username
            )

        except Exception as e:

            # IMPORTANT:
            # Do NOT call Tkinter directly from this thread.

            error_message = str(e)

            self.gui_queue.put(
                (
                    "error",
                    error_message
                )
            )

    # =========================================================
    # CLIENT CONNECTED CALLBACK
    # =========================================================

    def client_connected(self):

        # This callback may come from VoiceClient's
        # background thread.

        self.gui_queue.put(
            (
                "connected",
                None
            )
        )

    # =========================================================
    # UPDATE CONNECTED STATUS
    # =========================================================

    def _update_connected(self):

        self.status.configure(
            text="Connected. Establishing secure channel...",
            text_color="lightgreen"
        )

    # =========================================================
    # SECURE CHANNEL CALLBACK
    # =========================================================

    def secure_channel_ready(self):

        # This callback may come from the receiver thread.
        #
        # Put the event into the queue instead of
        # directly modifying Tkinter.

        self.gui_queue.put(
            (
                "secure",
                None
            )
        )

    # =========================================================
    # OPEN DASHBOARD
    # =========================================================

    def open_dashboard(self):

        if self.dashboard is not None:

            return

        # -----------------------------------------------------
        # Create Dashboard
        # -----------------------------------------------------

        self.dashboard = VoiceMessengerGUI(
            self,
            self.client
        )

        # -----------------------------------------------------
        # Set Username
        # -----------------------------------------------------

        self.dashboard.set_username(
            self.client.username
        )

        # -----------------------------------------------------
        # Set Peer
        # -----------------------------------------------------

        if self.client.peer_name:

            self.dashboard.set_peer(
                self.client.peer_name
            )

        # -----------------------------------------------------
        # Connected
        # -----------------------------------------------------

        self.dashboard.connected()

        # -----------------------------------------------------
        # Secure
        # -----------------------------------------------------

        self.dashboard.secure()

        # -----------------------------------------------------
        # Hide Login Window
        # -----------------------------------------------------

        self.withdraw()

    # =========================================================
    # CONNECTION FAILED
    # =========================================================

    def connection_failed(self, message):

        self.status.configure(
            text=f"❌ {message}",
            text_color="red"
        )

        self.connect_btn.configure(
            state="normal"
        )

        self.username.configure(
            state="normal"
        )

        self.host.configure(
            state="normal"
        )

        self.port.configure(
            state="normal"
        )


# =============================================================
# START APPLICATION
# =============================================================

if __name__ == "__main__":

    app = LoginWindow()

    app.mainloop()