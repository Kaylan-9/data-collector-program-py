import os
from dotenv import load_dotenv, find_dotenv
from playwright.sync_api import sync_playwright
from openpyxl import Workbook

load_dotenv(find_dotenv())

def collect(page):
  page.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/span').click()
  page.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/a').click()
  page.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]').click()
  text = page.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div[1]/div/div[2]/div/span').text_content()
  page.wait_for_timeout(9000)
  return text

def login(page):
  useremail = os.environ.get('EMA')
  password = os.environ.get('PAS')
  page.locator('xpath=//*[@id="email"]').fill(useremail)
  page.locator('xpath=//*[@id="pass"]').fill(password)
  page.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

def create_spreadsheet(data):
  wb = Workbook()
  ws = wb.active
  ws['A1'] = data
  wb.save("data.xlsx")

def init(p):
  url = os.environ.get('URL')
  browser = p.chromium.launch()
  page = browser.new_page()
  page.goto(url)
  login(page)
  data = collect(page)
  create_spreadsheet(data)
  browser.close()

with sync_playwright() as p:
  try:
    init(p)
  except ValueError:
    print(ValueError)
    
