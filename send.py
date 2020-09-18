import smtplib

server = smtplib.SMTP_SSL('smtp.ukr.net', 2525)
server.login("vladislv31@ukr.net", "abcv1234")
server.sendmail(
  "vladislv31@ukr.net", 
  "luckylitestudio@gmail.com", 
  "this message is from python")
server.quit()
