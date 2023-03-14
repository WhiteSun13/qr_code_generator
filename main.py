import qrcode
img = qrcode.make('Github Webhook')
img.save("github_webhook.png")
