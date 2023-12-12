import flet as ft
from supabase import create_client, Client

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMDM0NjYsImV4cCI6MjAxNzY3OTQ2Nn0.FDdQRXgW-_rMqIP4g5ttRwbynr-APBIlg_oFuVoOyww"
supabase: Client = create_client(url, key)


def main(page: ft.Page):
    page.padding = 0
    page.horizontal_alignment = "center"
    logo_img = ft.Image(
        src=f"/testing.jpg", width=1000, height=140, fit=ft.ImageFit.COVER
    )

    txt_email = ft.TextField(
        label="EMAIL",
        hint_text="Masukkan Email...",
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE,
        border=ft.InputBorder.UNDERLINE,
        suffix_icon=ft.icons.EMAIL,
        cursor_color=ft.colors.BLUE,
        keyboard_type=ft.KeyboardType.EMAIL,
    )

    txt_password = ft.TextField(
        label="PASSWORD",
        hint_text="Masukkan Password...",
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE,
        border=ft.InputBorder.UNDERLINE,
        password=True,
        can_reveal_password=True,
    )

    txt_nim = ft.TextField(
        label="NIM",
        hint_text="Masukkan NIM...",
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE,
        border=ft.InputBorder.UNDERLINE,
        cursor_color=ft.colors.BLUE,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    txt_username = ft.TextField(
        label="USERNAME",
        hint_text="Masukkan Username...",
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE,
        border=ft.InputBorder.UNDERLINE,
        suffix_icon=ft.icons.TAG_FACES,
        cursor_color=ft.colors.BLUE,
    )

    def register(e):
        email = txt_email.value
        password = txt_password.value
        nim = txt_nim.value
        username = txt_username.value

        res = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "nim": nim,
                        "username": username,
                    }
                },
            }
        )

    page.add(
        ft.Container(
            content=ft.Stack(
                [
                    ft.Container(content=logo_img, right=40, left=40, top=40),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(
                                    "Buat Akun",
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.BOLD,
                                    size=30,
                                ),
                            ],
                            alignment="center",
                        ),
                        top=250,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(
                                    "Mari buat akun presence-mu",
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.W_200,
                                    size=15,
                                ),
                            ],
                            alignment="center",
                        ),
                        top=305,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                txt_username,
                                txt_nim,
                                txt_email,
                                txt_password,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        top=340,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Buat Akun",
                                    color=ft.colors.WHITE,
                                    bgcolor="#94D3E4",
                                    width=250,
                                    height=50,
                                    on_click=register,
                                ),
                            ],
                            alignment="center",
                        ),
                        width=1000,
                        top=630,
                        right=50,
                        left=50,
                    ),
                ],
                expand=True,
                width=14000,
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#00BAE9", ft.colors.WHITE],
                stops=[0.2, 0.55],
            ),
            width=14000,
            expand=True,
        )
    )


ft.app(target=main, assets_dir="asset")
