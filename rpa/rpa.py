import time
import datetime
import environs


from selenium import webdriver

env = environs.Env()
env.read_env()


def check_date():
    date = datetime.date.today() - datetime.timedelta(month=1)

    return date.strftime('%m/%Y')


def issue_invoice():
    navegator = webdriver.Chrome(env('WEBDRIVER'))
    # Login
    navegator.get(env('URL'))
    time.sleep(2)

    navegator.find_element_by_id('j_idt29:j_idt37_content').click()
    time.sleep(2)

    navegator.find_element_by_id('frmLogin:j_idt34').click()
    time.sleep(2)

    navegator.find_element_by_id('frmLogin:cnpj_cpf_login').send_keys(env('CNPJ'))
    navegator.find_element_by_id('frmLogin:password').send_keys(env('PASSWORD'))
    navegator.find_element_by_id('frmLogin:j_idt39').click()
    time.sleep(3)

    # NFS-e
    navegator.find_element_by_xpath(
        '//*[@id="j_idt35:j_idt36:j_idt38"]/a[2]/table/tbody/tr/td[2]'
    ).click()
    time.sleep(2)

    # Buscar tomador.
    navegator.find_element_by_xpath('//*[@id="formGeral:txtDocTomador"]').send_keys(
        env('TOMADOR')
    )
    navegator.find_element_by_id('formGeral:j_idt197').click()
    time.sleep(2)

    # Preencher nota.
    navegator.find_element_by_xpath(
        '//*[@id="formGeral:tvGeral"]/div[1]/ul/li[2]/a'
    ).click()
    time.sleep(2)

    navegator.find_element_by_id('formGeral:tvGeral:j_idt272').send_keys(
        env('MESSAGE') + check_date()
    )

    valor = navegator.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div[4]/div/div/form/div/div[2]/div[3]/div[2]/div[2]/table[5]/tbody/tr[2]/td[2]/input'
    )
    valor.clear()
    valor.send_keys(env('PAY'))

    navegator.find_element_by_xpath(
        '//*[@id="formGeral:tvGeral:cbtGerarRelatorio"]/span[2]'
    ).click()
    time.sleep(2)

    navegator.find_element_by_xpath(
        '//*[@id="formDialogConfirmaDadosBotoes:j_idt710"]/span[2]'
    ).click()

    return
