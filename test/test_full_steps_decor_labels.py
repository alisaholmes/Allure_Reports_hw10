import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Автотест с Allure")
@allure.story("Проверка Issues в github-репозитории")
@allure.link("https://github.com", name="Testing")

def test_decorator_steps():
    open_page()
    search_for_repository("alisaholmes/Allure_Reports_hw10")
    open_issue_tab()
    should_see_issue_with_name(name="Welcome to issues!")


@allure.step("Открываем главную страницу")
def open_page():
    browser.open("/")


@allure.step("Ищем репозиторий и переходим в него")
def search_for_repository(alisaholmes):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys(alisaholmes).press_enter()
    browser.element(by.link_text(alisaholmes)).click()

@allure.step("Открываем Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие в Issues текста Welcome to issues!")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).should(be.visible)




