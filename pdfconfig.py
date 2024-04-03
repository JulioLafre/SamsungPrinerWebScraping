from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from baseimpressoras import Impressora
from datetime import datetime

def criar_pdf_impressora(impressora: Impressora, nome_arquivo="informacoes_impressora.pdf"):
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    width, height = letter  # Tamanho padrão da página (carta)

    # Configurações básicas para o PDF
    c.setFont("Helvetica-Bold", 16)
    y_pos = height - 50
    c.drawString(40, y_pos, "Printer Information")
    
    # Aumenta o espaço entre o título e a linha
    y_pos -= 25
    c.line(40, y_pos, width - 40, y_pos)
    
    # Aumenta o espaço entre a linha e o subtítulo
    y_pos -= 30
    c.setFont("Helvetica", 12)
    c.drawString(40, y_pos, "General Information")

    # Informações da Impressora
    c.setFont("Helvetica", 10)
    y_pos -= 15
    infos = [
    ("Date/Time", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),  # Formatação da data e hora
    ("Model Name", impressora.modelo),
    ("Machine Serial Number", impressora.numero_serie),
    ("Host Name", impressora.host),
    ("Total Impressions", impressora.total_impressoes),
    ]

    for label, value in infos:
        c.drawString(80, y_pos, f"{label}: {value}")
        y_pos -= 12

    # Subtítulo para Informações do Toner
    y_pos -= 20
    c.setFont("Helvetica", 12)
    c.drawString(40, y_pos, "Toner Information")

    c.setFont("Helvetica", 10)
    y_pos -= 15
    toner_infos = [
        ("Model ID", impressora.modelo_toner),
        ("Life Remaining", impressora.vida_restante_toner),
        ("Impressions", impressora.total_impressoes_toner),
        ("Serial Number", impressora.numero_serie_toner),
        ("Capacity", impressora.capacidade_toner),
        # Adicione mais informações do toner conforme necessário
    ]

    for label, value in toner_infos:
        c.drawString(80, y_pos, f"{label}: {value}")
        y_pos -= 12

    # Subtítulo para Vida Útil de Outros Consumíveis
    y_pos -= 20
    c.setFont("Helvetica", 12)
    c.drawString(40, y_pos, "Other Consumables Life")

    c.setFont("Helvetica", 10)
    y_pos -= 15
    other_infos = [
        ("Fuser Life", impressora.vida_util_fusor),
        ("Transfer Roller Life", impressora.vida_util_rolo_transferencia),
        ("Tray 1 Roller Life", impressora.vida_util_rolo_bandeja_um),
        ("Tray 1 Retard Roller Life", impressora.vida_util_rolo_retrocesso_bandeja_um),
        ("MP Roller Life", impressora.vida_util_bandeja_multifuncional),
        ("MP Retard Roller Life", impressora.vida_util_rolo_bandeja_multifuncional)
        # Adicione mais informações sobre outros consumíveis conforme necessário
    ]

    for label, value in other_infos:
        c.drawString(80, y_pos, f"{label}: {value}")
        y_pos -= 12

    # Finaliza o documento
    c.save()