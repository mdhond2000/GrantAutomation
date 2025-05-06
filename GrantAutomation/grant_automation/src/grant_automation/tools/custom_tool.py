def send_email_tool(report: str) -> str:
    import smtplib
    from email.mime.text import MIMEText

    sender = "mdd013002@gmail.com"
    password = "oeymqkoyejkxpmnb"  # Gmail App Password
    recipient = "pmohanraj@healthtechalley.org"

    # Customize your message content here:
    body = f"""\
{report}

If you have any questions or would like to discuss next steps, feel free to reach out.

Best regards,  
Final Report Manager  
Health Tech Alley
"""

    msg = MIMEText(body, "plain")
    msg["Subject"] = "Finalized Grant Report for Review"
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        return "✅ Email sent successfully"
    except Exception as e:
        return f"❌ Failed to send email: {e}"
