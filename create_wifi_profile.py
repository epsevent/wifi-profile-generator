import uuid
import os

# ===== AYARLAR =====
SSID = os.getenv("WIFI_SSID", "MyWiFi")  # Actions secret'tan gelecek
PASSWORD = os.getenv("WIFI_PASS", "12345678")
ENCRYPTION = "WPA2"

# ===== UUID ÜRET =====
wifi_uuid = str(uuid.uuid4()).upper()
profile_uuid = str(uuid.uuid4()).upper()

# ===== XML ŞABLONU =====
template = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>PayloadContent</key>
   <array>
      <dict>
         <key>AutoJoin</key>
         <true/>
         <key>EncryptionType</key>
         <string>{ENCRYPTION}</string>
         <key>HIDDEN_NETWORK</key>
         <false/>
         <key>PayloadDescription</key>
         <string>Wi-Fi configuration</string>
         <key>PayloadDisplayName</key>
         <string>{SSID}</string>
         <key>PayloadIdentifier</key>
         <string>com.onur.wifi</string>
         <key>PayloadType</key>
         <string>com.apple.wifi.managed</string>
         <key>PayloadUUID</key>
         <string>{wifi_uuid}</string>
         <key>PayloadVersion</key>
         <integer>1</integer>
         <key>SSID_STR</key>
         <string>{SSID}</string>
         <key>Password</key>
         <string>{PASSWORD}</string>
      </dict>
   </array>
   <key>PayloadDisplayName</key>
   <string>Wi-Fi Setup</string>
   <key>PayloadIdentifier</key>
   <string>com.onur.wifi.profile</string>
   <key>PayloadRemovalDisallowed</key>
   <false/>
   <key>PayloadType</key>
   <string>Configuration</string>
   <key>PayloadUUID</key>
   <string>{profile_uuid}</string>
   <key>PayloadVersion</key>
   <integer>1</integer>
</dict>
</plist>"""

# ===== DOSYA KAYDET =====
filename = "wifi.mobileconfig"  # Sabit dosya adı
with open(filename, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ {filename} oluşturuldu.")
