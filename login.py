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
        password=True,
        can_reveal_password=True,
        hint_text="Masukkan Password...",
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE,
        border=ft.InputBorder.UNDERLINE,
    )

    txt_error = ft.Text(
        "Email atau password salah!",
        color=ft.colors.RED,
        opacity=0,
    )

    def login(e):
        nim = txt_email.value
        password = txt_password.value

        try:
            res = supabase.auth.sign_in_with_password(
                {"email": nim, "password": password}
            )
            txt_email.value, txt_password.value = "", ""
            page.update()

        except:
            txt_email.value, txt_password.value = "", ""

            txt_error.opacity = 100
            page.update()

    page.add(
        ft.Container(
            content=ft.Stack(
                [
                    ft.Container(content=logo_img, right=40, left=40, top=40),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(
                                    "Log In",
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
                                    "Absen Kehadiranmu dengan presence",
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
                            [txt_email, txt_password, txt_error],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
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
                                    "Log In",
                                    color=ft.colors.WHITE,
                                    bgcolor="#94D3E4",
                                    width=250,
                                    height=50,
                                    on_click=login,
                                ),
                            ],
                            alignment="center",
                        ),
                        width=1000,
                        top=600,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(
                                    "Belum punya akun?",
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.W_600,
                                ),
                                ft.TextButton(
                                    "Register",
                                ),
                            ],
                            alignment="center",
                        ),
                        width=1000,
                        top=655,
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
