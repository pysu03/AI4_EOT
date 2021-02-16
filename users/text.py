def message(domain, uidb64, token):
    return f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다. \n\n 회원가입 링크 : http://{domain}/users/{uidb64}/{token}\n\n 감사합니다"