from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.units import cm


def generate_table_pdf(response, title, headers, rows):

    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1*cm,
        topMargin=1*cm,
        bottomMargin=1*cm,
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b><font size=18>Université - Projet MIAGE</font></b>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(title, styles["Heading2"])
    )

    elements.append(Spacer(1, 0.5*cm))

    data = [headers]

    for row in rows:
        data.append(row)

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("FONTSIZE", (0,0), (-1,-1), 9),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("ALIGN", (0,0), (-1,-1), "CENTER"),

            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),

            ("BOTTOMPADDING", (0,0), (-1,0), 10),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

        ])

    )

    elements.append(table)

    doc.build(elements)