# -*- coding: utf-8 -*-

# importa biblioteca
import fitz
import re

conteudo = ""

with fitz.open("arquivo.pdf") as pdf:

    for pagina in pdf:
        conteudo += pagina.get_text()

# remove o parte inicial => começar na introdução
inicio = conteudo.find('Introduction')
conteudo = conteudo[inicio:]

# remove cabeçalho
cabecalho = "Encyclopedia 2022, 2, FOR PEER REVIEW" #alterar este campo
conteudo = conteudo.replace(cabecalho, '')

# remove as referencias
fim = conteudo.find('References')
conteudo = conteudo[:fim]
# conteudo = conteudo.replace('\n138\n \n','')

# remove quebras de linhas
# conteudo = re.sub('\n','', conteudo) 

# remove quebras de linhas com número no fim
conteudo = re.sub('\n[0-9]{1,4}\n \n','', conteudo) 

# print(conteudo2)

analise = conteudo.split('.')
# print(len(analise)) # total de frases => 359

frases = []
for i in analise:
    if len(i) > 10:  # remove frases com menos de 10 letras
        # print('\n::INICIO::\n',i,'\n::FIM::\n', len(i))
        frases.append(i)

print('Total de frases:', len(frases))

tamanho_frases = []
for i in frases:
    aux = i.split()
    # if len(aux) > 50:
    #     print(i)
    print(i)
    # print(len(aux))






# add_caret_annot
# add_circle_annot
# add_file_annot
# add_freetext_annot
# add_highlight_annot
# add_ink_annot
# add_line_annot
# add_polygon_annot
# add_polyline_annot
# add_rect_annot
# add_redact_annot
# add_squiggly_annot
# add_stamp_annot
# add_strikeout_annot
# add_text_annot
# add_underline_annot
# add_widget
# annot_names
# annot_xrefs
# annots
# apply_redactions
# artbox
# bleedbox
# bound
# clean_contents
# cropbox
# cropbox_position
# delete_annot
# delete_link
# delete_widget
# derotation_matrix
# draw_bezier
# draw_circle
# draw_curve
# draw_line
# draw_oval
# draw_polyline
# draw_quad
# draw_rect
# draw_sector
# draw_squiggle
# draw_zigzag
# extend_textpage
# first_annot
# first_link
# first_widget
# get_bboxlog
# get_cdrawings
# get_contents
# get_displaylist
# get_drawings
# get_fonts
# get_image_bbox
# get_image_info
# get_image_rects
# get_images
# get_label
# get_links
# get_oc_items
# get_pixmap
# get_svg_image
# get_text
# get_text_blocks
# get_text_selection
# get_text_words
# get_textbox
# get_textpage
# get_textpage_ocr
# get_texttrace
# get_xobjects
# insert_font
# insert_image
# insert_link
# insert_text
# insert_textbox
# is_wrapped
# language
# links
# load_annot
# load_links
# load_widget
# mediabox
# mediabox_size
# new_shape
# number
# parent
# read_contents
# rect
# refresh
# rotation
# rotation_matrix
# run
# search_for
# set_artbox
# set_bleedbox
# set_contents
# set_cropbox
# set_language
# set_mediabox
# set_rotation
# set_trimbox
# show_pdf_page
# this
# thisown
# transformation_matrix
# trimbox
# update_link
# widgets
# wrap_contents
# write_text
# xref
