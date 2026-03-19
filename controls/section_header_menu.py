# from controls.base_control import BaseControl
#
# class SectionMenu(BaseControl):
#     """
#     Часть верхнего меню, где представлены разделы: главная, каталог, обратная связь, ЛК
#     """
#     def __init__(self, page, wrapper):
#         super().__init__(page, page.locator('nav'))
#
#     def section_by_title(self, title):
#         self.page.locator(f"a:has-text('{title}')")
#
#     def section_by_home(self):
#         self.page.locator('.home')
