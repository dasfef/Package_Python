import smtplib
from email.mime.text import MIMEText

send_email = "네이버메일@naver.com"
send_pwd = "네이버비밀번호"

recv_email = "받는이메일주소@hanmail.net"

smtp_name = "smtp.naver.com" 
smtp_port = 587

text = """
메일 내용은
아두이노에서 버튼을 누르면 
파이썬으로 이메일을 보냅니다.
"""
msg = MIMEText(text)

msg['Subject'] ="메일 제목은 파이썬으로 이메일 보내기"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()