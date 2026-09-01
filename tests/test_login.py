from playwright.sync_api import expect
import pytest
from pages.login_page import LoginPage

def test_page_has_correct_title(page):
    page.goto("https://the-internet.herokuapp.com")
    expect(page).to_have_title("The Internet")


def test_abtest_page_title(page):
    page.goto("https://the-internet.herokuapp.com/abtest")
    expect(page).to_have_title("The Internet")

def test_add_remove_heding(page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    heading = page.locator("h3")
    expect(heading).to_have_text("Add/Remove Elements")

def test_checkboxes_heading(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    mainheader = page.locator("h3")
    expect(mainheader).to_have_text("Checkboxes")

def test_dynamic_loading(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.click("button")
    finish_text = page.locator("#finish")
    expect(finish_text).to_be_visible(timeout=10000)
    expect(finish_text).to_have_text("Hello World!")

def test_dynamic_loading_podvoh(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.click("button")
    element = page.locator("#finish")
    expect(element).to_be_visible(timeout=10000)
    expect(element).to_have_text("Hello World!")


def test_first_checkbox_can_be_checked(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    first_checkbox = checkboxes.nth(0)
    expect(first_checkbox).not_to_be_checked()
    first_checkbox.check()
    expect(first_checkbox).to_be_checked()

def test_second_checkbox_can_be_checked(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    secondcheckbox = checkboxes.nth(1)
    expect(secondcheckbox).to_be_checked()
    secondcheckbox.uncheck()
    expect(secondcheckbox).not_to_be_checked()

def test_select_option_2_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("2")
    expect(dropdown).to_have_value("2")

def test_select_option_1_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")

def test_js_alert_ok(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("text=Click for JS Alert")
    result = page.locator("#result")
    expect(result).to_have_text("You successfully clicked an alert")



def test_js_confirm_accept(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("text=Click for JS Confirm")
    result = page.locator("#result")
    expect(result).to_have_text("You clicked: Ok")

def test_hover_shows_user_info(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    first_image = page.locator(".figure").nth(0)
    first_image.hover()
    caption = first_image.locator("h5")
    expect(caption).to_be_visible()
    expect(caption).to_have_text("name: user1")

def test_hover_second_user_shows_info(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    second_image = page.locator(".figure").nth(1)
    second_image.hover()
    caption = second_image.locator("h5")
    expect(caption).to_be_visible()
    expect(caption).to_have_text("name: user2")

def test_drug_and_drop(page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    column_a = page.locator("#column-a")
    column_b = page.locator("#column-b")
    column_a.drag_to(column_b)
    expect(column_a).to_have_text("B")
    expect(column_b).to_have_text("A")

def test_drag_and_drop_reverse(page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    column_a = page.locator("#column-a")
    column_b = page.locator("#column-b")
    column_b.drag_to(column_a)
    expect(column_b).to_have_text("A")
    expect(column_a).to_have_text("B")

def test_upload_file(page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files("test_files/example.txt")
    page.click("#file-submit")
    uploaded_text = page.locator("#uploaded-files")
    expect(uploaded_text).to_have_text("example.txt")

def test_second_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files("test_files/second.txt")
    page.click("#file-submit")
    uploaded_text = page.locator("#uploaded-files")
    expect(uploaded_text).to_have_text("second.txt")

def test_number_input(page):
    page.goto("https://the-internet.herokuapp.com/inputs")
    number_input = page.locator("input")
    number_input.fill("42")
    expect(number_input).to_have_value("42")


def test_number_input_negative(page):
    page.goto("https://the-internet.herokuapp.com/inputs")
    input_field = page.locator("input")
    input_field.fill("-15")
    expect(input_field).to_have_value("-15")

def test_new_window_opens(page):
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.context.expect_page() as new_page_info:page.click("text=Click Here")
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_title("New Window")

def test_new_window_url(page):
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.context.expect_page() as new_page_info:page.click("text=Click Here")
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://the-internet.herokuapp.com/windows/new")

def test_iframe_text(page):
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")
    expect(editor).to_have_text("Your content goes here.")

def test_iframe_editable(page):
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")
    editor.click()
    editor.fill("I did it")
    expect(editor).to_have_text("I did it")



def test_login_succes(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator(".flash.success")).to_be_visible()

def test_login_failure(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "invalidname")
    page.fill("#password", "invalidpass")
    page.click("button[type='submit']")
    expect(page.locator(".flash.error")).to_be_visible()

@pytest.mark.parametrize("username, password, expected_message", [
    ("tomsmith", "SuperSecretPassword!", "success"),
    ("tomsmith", "", "error"),
    ("", "SuperSecretPassword!", "error"),
    ("wrongname", "SuperSecretPassword!", "error"),
    ("tomsmith", "wrongpass", "error")
])

def test_login_parametrized(page, username, password, expected_message):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")
    expect(page.locator(f".flash.{expected_message}")).to_be_visible()

def test_login_success_with_pom(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
