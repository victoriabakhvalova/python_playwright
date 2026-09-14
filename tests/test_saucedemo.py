from playwright.sync_api import expect
import pytest
from pages.login_page import LoginPage
from pages.login_page_saucedemo import LoginPage

def test_saucedemo_login_positive(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_fail_saucedemo_login(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("IncorrectName")
    page.get_by_placeholder("Password").fill("incorrectPassword")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("[data-test='error']")).to_be_visible()


def test_items_list_show(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_item").first).to_be_visible()

def test_sauce_labs_present(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_add_to_cart_counter(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.get_by_role("button", name="Add to cart").nth(2).click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

def test_check_items_in_a_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Fleece Jacket")).to_be_visible()

def test_delete_from_cart(page):
    page.goto("https://www.saucedemo.com/")

    #login
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    #add to cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()

    #check cart
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Fleece Jacket")).to_be_visible()

    #remove from cart
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    page.locator('[data-test="remove-sauce-labs-fleece-jacket"]').click()

    #expected result
    expect(page.get_by_text("Sauce Labs Backpack")).not_to_be_visible()
    expect(page.get_by_text("Sauce Labs Fleece Jacket")).not_to_be_visible()





