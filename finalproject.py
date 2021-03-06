import smtplib
f = open ("email.txt", "w")         #sbg file handling receveir
f.write("tiarapratiwi73.tp@gmail.com \n"
        "syamart116@gmail.com")
f.close() #ini utk tambahan penutup


mail_sender = "tiarapratiwi73.tp@gmail.com"
mail_receiver = "syamart116@gmail.com"
mail_subject = " tes "
mail_body = " abc "

mail_msg = ("from: {} \n to: {} \n subject: {} \n message: {} \n".format(mail_sender, mail_receiver,mail_subject,mail_body))
