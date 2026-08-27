import customtkinter as ctk
import threading
import queue


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class VoiceMessengerGUI(ctk.CTkToplevel):

    def __init__(self,parent, client):

        super().__init__(parent)

        self.parent=parent
        self.client = client
        self.gui_queue = queue.Queue()

        self.title("🔒 Secure Voice Messenger")
        self.geometry("1000x700")
        self.resizable(False, False)

        self.build_gui()
        self.bind_callbacks()
        self.after(
            50,
           self.process_gui_events
         )

    # =========================================================
    # BUILD GUI
    # =========================================================

    def build_gui(self):

        # =====================================================
        # HEADER
        # =====================================================

        header = ctk.CTkFrame(
            self,
            height=80
        )

        header.pack(
            fill="x",
            padx=15,
            pady=15
        )

        title = ctk.CTkLabel(
            header,
            text="🔒 Secure Voice Messenger",
            font=("Arial", 28, "bold")
        )

        title.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.connection = ctk.CTkLabel(
            header,
            text="🔴 Offline",
            font=("Arial", 18, "bold"),
            text_color="red"
        )

        self.connection.pack(
            side="right",
            padx=20
        )

        # =====================================================
        # INFORMATION
        # =====================================================

        info = ctk.CTkFrame(self)

        info.pack(
            fill="x",
            padx=15
        )

        self.user = ctk.CTkLabel(
            info,
            text="User : -",
            font=("Arial", 16)
        )

        self.user.grid(
            row=0,
            column=0,
            padx=30,
            pady=15
        )

        self.peer = ctk.CTkLabel(
            info,
            text="Peer : -",
            font=("Arial", 16)
        )

        self.peer.grid(
            row=0,
            column=1,
            padx=30,
            pady=15
        )

        self.encryption = ctk.CTkLabel(
            info,
            text="Encryption : AES-256-GCM",
            font=("Arial", 16)
        )

        self.encryption.grid(
            row=1,
            column=0,
            padx=30,
            pady=10
        )

        self.session = ctk.CTkLabel(
            info,
            text="Session : Not Secure",
            font=("Arial", 16),
            text_color="orange"
        )

        self.session.grid(
            row=1,
            column=1,
            padx=30,
            pady=10
        )

        # =====================================================
        # ACTIVITY LOG
        # =====================================================

        log_frame = ctk.CTkFrame(self)

        log_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        log_title = ctk.CTkLabel(
            log_frame,
            text="Activity Log",
            font=("Arial", 20, "bold")
        )

        log_title.pack(pady=10)

        self.logs = ctk.CTkTextbox(
            log_frame,
            width=900,
            height=250
        )

        self.logs.pack(
            padx=20,
            pady=10
        )

        # Prevent manual editing
        self.logs.configure(
            state="disabled"
        )

        # =====================================================
        # PROGRESS BAR
        # =====================================================

        self.progress = ctk.CTkProgressBar(
            self,
            width=700
        )

        self.progress.pack(
            pady=10
        )

        self.progress.set(0)

        # =====================================================
        # BUTTONS
        # =====================================================

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            padx=15,
            pady=15
        )

        # Record
        self.record_btn = ctk.CTkButton(
            buttons,
            text="🎤 Record Voice",
            width=220,
            height=45,
            state="disabled",
            command=self.record_voice
        )

        self.record_btn.grid(
            row=0,
            column=0,
            padx=25,
            pady=20
        )

        # Send
        self.send_btn = ctk.CTkButton(
            buttons,
            text="📤 Send Voice",
            width=220,
            height=45,
            state="disabled",
            command=self.send_voice
        )

        self.send_btn.grid(
            row=0,
            column=1,
            padx=25,
            pady=20
        )

        # Play
        self.play_btn = ctk.CTkButton(
            buttons,
            text="▶ Play Last Voice",
            width=220,
            height=45,
            state="disabled",
            command=self.play_last_voice
        )

        self.play_btn.grid(
            row=0,
            column=2,
            padx=25,
            pady=20
        )

        # =====================================================
        # FOOTER
        # =====================================================

        footer = ctk.CTkLabel(
            self,
            text="End-to-End Encryption using X25519 + AES-256-GCM",
            font=("Arial", 14)
        )

        footer.pack(
            pady=10
        )

    # =========================================================
    # CALLBACK BINDING
    # =========================================================

    def bind_callbacks(self):

        self.client.on_log = self.log

        self.client.on_connected = self.connected

        self.client.on_secure = self.secure

        self.client.on_voice_received = self.voice_received

    # =========================================================
    # LOGGING
    # =========================================================

    def log(self, message):

        self.gui_queue.put(
        ("log", message)
        )

    def _update_log(self, message):

        self.logs.configure(
            state="normal"
        )

        self.logs.insert(
            "end",
            message + "\n"
        )

        self.logs.see(
            "end"
        )

        self.logs.configure(
            state="disabled"
        )


    def process_gui_events(self):

      try:

        while True:

            event, data = self.gui_queue.get_nowait()

            if event == "log":

                self._update_log(data)

            elif event == "connected":

                self._update_connected()

            elif event == "secure":

                self._update_secure()

            elif event == "voice_received":

                self._update_voice_received()

            
            elif event == "record_complete":

                 self.progress.set(0.50)

                 self.record_btn.configure(
                       state="normal"
                    )

                 self.send_btn.configure(
                  state="normal"
                 )

            elif event == "send_complete":

             self.progress.set(1)

             self.send_btn.configure(
               state="normal"
              )

      except queue.Empty:

        pass

    # Schedule next check
      self.after(
        50,
        self.process_gui_events
      )

    # =========================================================
    # CONNECTED
    # =========================================================

    def connected(self):

         
         self.gui_queue.put(
        ("connected", None)
    )


        

    def _update_connected(self):

        self.connection.configure(
            text="🟢 Connected",
            text_color="lightgreen"
        )

        

    # =========================================================
    # SECURE CHANNEL
    # =========================================================

    def secure(self):

     self.gui_queue.put(
        ("secure", None)
    )


    def _update_secure(self):

      self.session.configure(
        text="Session : Secure",
        text_color="lightgreen"
    )

      self.progress.set(1)

      self.record_btn.configure(
        state="normal"
    )

      self.send_btn.configure(
        state="normal"
    )

      self.play_btn.configure(
        state="normal"
    )

    # =========================================================
    # VOICE RECEIVED
    # =========================================================

    def voice_received(self):
         self.gui_queue.put(
        ("voice_received", None)
    )

        

    def _update_voice_received(self):

        self.progress.set(1)

        self.log(
            "🎵 Voice message received and played."
        )

    # =========================================================
    # RECORD VOICE
    # =========================================================

    def record_voice(self):

        if not self.client.secure_channel:

            self.log(
                "Secure channel not established."
            )

            return

        self.record_btn.configure(
            state="disabled"
        )

        self.send_btn.configure(
            state="disabled"
        )

        self.progress.set(
            0.25
        )

        self.log(
            "🎤 Recording Voice..."
        )

        threading.Thread(
            target=self._record_voice_thread,
            daemon=True
        ).start()


    def _record_voice_thread(self):

       try:

        success = self.client.record_voice()

        if success:

            self.gui_queue.put(
                ("log", "✓ Recording Complete")
            )

            self.gui_queue.put(
                ("record_complete", None)
            )

        else:

            self.gui_queue.put(
                ("log", "Recording failed.")
            )

       except Exception as e:

        self.gui_queue.put(
            ("log", f"Recording Error: {e}")
        )

        self.gui_queue.put(
            ("record_complete", None)
        )

    # =========================================================
    # SEND VOICE
    # =========================================================

    def send_voice(self):

        if not self.client.secure_channel:

            self.log(
                "Secure channel not established."
            )

            return

        if self.client.audio_data is None:

            self.log(
                "No recorded voice available."
            )

            return

        self.send_btn.configure(
            state="disabled"
        )

        self.progress.set(
            0.75
        )

        threading.Thread(
            target=self._send_voice_thread,
            daemon=True
        ).start()



    def _send_voice_thread(self):

      try:

        success = self.client.send_recorded_voice()

        if success:

            self.gui_queue.put(
                (
                    "log",
                    "📤 Encrypted Voice Sent"
                )
            )

            self.gui_queue.put(
                (
                    "send_complete",
                    None
                )
            )

        else:

            self.gui_queue.put(
                (
                    "log",
                    "Voice transmission failed."
                )
            )

            self.gui_queue.put(
                (
                    "send_complete",
                    None
                )
            )

      except Exception as e:

        error_message = str(e)

        self.gui_queue.put(
            (
                "log",
                f"Send Error: {error_message}"
            )
        )

        self.gui_queue.put(
            (
                "send_complete",
                None
            )
        )

    # =========================================================
# PLAY LAST VOICE
# =========================================================

    def play_last_voice(self):

      threading.Thread(
        target=self._play_voice_thread,
        daemon=True
      ).start()


    def _play_voice_thread(self):

      try:

        self.client.play_last_voice()

        self.gui_queue.put(
            (
                "log",
                "▶ Playing last received voice."
            )
        )

      except Exception as e:

        error_message = str(e)

        self.gui_queue.put(
            (
                "log",
                f"Playback Error: {error_message}"
            )
        )
    # =========================================================
    # USERNAME
    # =========================================================

    def set_username(self, username):

        self.user.configure(
            text=f"User : {username}"
        )

    # =========================================================
    # PEER
    # =========================================================

    def set_peer(self, peer):

        self.peer.configure(
            text=f"Peer : {peer}"
        )