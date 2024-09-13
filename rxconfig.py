import reflex as rx

config = rx.Config(
    app_name="sisvivi",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://sisvivi.vercel.app"
    ]
)