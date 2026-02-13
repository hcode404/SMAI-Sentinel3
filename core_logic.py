# SMAI Sentinel Core Logic v1.0
# Monitoring suspicious patterns in Roblox chat logs

def smai_security_scan(message):
    # מילות מפתח שמרמזות על ניסיון הונאה או הטרדה
    danger_zone = ["robux", "password", "hack", "discord", "meet", "whatsapp"]
    
    found_threats = [word for word in danger_zone if word in message.lower()]
    
    if found_threats:
        return f"🚨 SMAI ALERT: Suspicious activity detected! Found: {found_threats}"
    return "✅ Message clear."

# בדיקה קצרה
chat_example = "Hey, go to this site for free robux and enter your password"
print(smai_security_scan(chat_example))
