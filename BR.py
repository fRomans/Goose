# import flet as ft
#
#
# class BoevRasch(ft.UserControl):
#     fff = ''
#     def build(self):
#
#         self.t = ft.Text(value='Укажи какая смена заступает')
#         self.b = ft.ElevatedButton(text='Начать формирование БР', on_click=self.add_clicked)
#         self.cg = ft.RadioGroup(content=ft.Row([
#             ft.Radio(value="1",label="1 смена"),
#             ft.Radio(value="2", label="2 смена"),
#             ft.Radio(value="3",label="3 смена"),
#             ft.Radio(value="4",label="4 смена"),
#             ft.Radio(value="5", label="5 смена")]))
#
#         return ft.Column(
#             width=600,
#             controls=[
#                 self.t,
#                 ft.Row(
#                     controls=[
#                         self.cg,
#                     ],
#                 ),
#                 self.b
#             ],
#         )
#
#
#     def add_clicked(self, e):
#         self.t.value = f"Your favorite color is: {self.cg.value}"
#         zastup_sm = str(self.cg.value)
#         print(zastup_sm)
#         self.update()
#
#
#
#
#
#
#
# def main(page: ft.Page):
#     page.title = "Бомбовый расчет"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.update()
#
#     boevRasch = BoevRasch()
#     page.add(boevRasch)
#
#
# ft.app(target=main)