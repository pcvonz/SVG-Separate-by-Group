text = input("what is your file name?")
f = open(text, "r+")
beginning = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Generator: Adobe Illustrator 16.0.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.1" id="Layer_1" x="0px" y="0px" width="124.00007" height="124" viewBox="0 0 124.00007 124" enable-background="new 0 0 1182.118 1164.116" xml:space="preserve" inkscape:version="0.48.5 r10040" sodipodi:docname="ResTek site icons_collapsed.svg">
    <metadata id="metadata4410">
        <rdf:RDF>
            <cc:Work rdf:about="">
                <dc:format>image/svg+xml</dc:format>
                <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
                <dc:title></dc:title>
            </cc:Work>
        </rdf:RDF>
    </metadata>
    <defs id="defs4408" />
    <sodipodi:namedview pagecolor="#ffffff" bordercolor="#666666" borderopacity="1" objecttolerance="10" gridtolerance="10" guidetolerance="10" inkscape:pageopacity="0" inkscape:pageshadow="2" inkscape:window-width="1920" inkscape:window-height="1138" id="namedview4406" showgrid="true" inkscape:zoom="2.8284271" inkscape:cx="84.931018" inkscape:cy="73.016218" inkscape:window-x="1672" inkscape:window-y="-8" inkscape:window-maximized="1" inkscape:current-layer="Layer_1" showguides="false" fit-margin-top="0" fit-margin-left="0" fit-margin-right="0" fit-margin-bottom="0">
        <inkscape:grid type="xygrid" id="grid4820" empspacing="5" visible="true" enabled="false" snapvisiblegridlinesonly="true" originx="-71.644277px" originy="-0.0016858216px" />
    </sodipodi:namedview>
'''
count = 0
white_space = 0
new_string = ""
filename = "new_svg"
name = 0
string = ""
string_test = ""
x = 0
g_count = 0
write_string = True

for line in f:
    string_test += line
f.seek(0)
for char in range(len(string_test)):
    #print(string_test[char])
    w = open(filename, "w+")
    if string_test[char] == "<":
        if string_test[char+1] == "g":
            g_count += 1
            print("\n\n\n\nWINNER")
            write_string = True
    if string_test[char] == "<":
        print("OH NO")
        if string_test[char+1] == "/":
            if string_test[char+2] == "g":
                g_count += -1
                if g_count == 0:
                    print("writing_file..")
                    write_string = False
                    w.write(beginning + "\n\n" + string + "</g>" + "\n" + "</svg>")
                    filename = str(x) + ".svg"
                    x += 1
                    w = open(filename, "w+")
                    string = ""
    if write_string == True:
        string += string_test[char]
print(string_test)

w.close()
f.close()
