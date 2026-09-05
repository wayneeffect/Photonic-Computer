#!/usr/bin/env python3
"""
Simple photonic time crystal logic gate schematic in DXF format.
Open-source, no external CAD libraries required.
Compatible with AutoCAD, LibreCAD, FreeCAD, QCAD, etc.
"""

def write_dxf(filename="ptc_logic_gate.dxf"):
    with open(filename, "w") as f:
        # DXF Header
        f.write("0\nSECTION\n2\nHEADER\n")
        f.write("9\n$ACADVER\n1\nAC1015\n")  # AutoCAD 2000 compatible
        f.write("9\n$INSUNITS\n70\n4\n")      # 4 = millimetres (we treat numbers as µm)
        f.write("0\nENDSEC\n")

        # Tables (minimal)
        f.write("0\nSECTION\n2\nTABLES\n")
        f.write("0\nTABLE\n2\nLAYER\n")
        f.write("0\nLAYER\n2\n0\n70\n0\n62\n7\n6\nCONTINUOUS\n")
        f.write("0\nLAYER\n2\nWAVEGUIDE\n70\n0\n62\n4\n6\nCONTINUOUS\n")      # Cyan
        f.write("0\nLAYER\n2\nPTC_REGION\n70\n0\n62\n6\n6\nCONTINUOUS\n")     # Magenta
        f.write("0\nLAYER\n2\nLABEL\n70\n0\n62\n2\n6\nCONTINUOUS\n")          # Yellow
        f.write("0\nLAYER\n2\nPUMP\n70\n0\n62\n1\n6\nDASHED\n")               # Red
        f.write("0\nENDTAB\n0\nENDSEC\n")

        # Entities
        f.write("0\nSECTION\n2\nENTITIES\n")

        # Helper to write a line
        def line(x1, y1, x2, y2, layer="WAVEGUIDE"):
            f.write(f"0\nLINE\n8\n{layer}\n10\n{x1}\n20\n{y1}\n11\n{x2}\n21\n{y2}\n")

        # Helper to write a rectangle (as closed polyline)
        def rect(x, y, w, h, layer="WAVEGUIDE"):
            f.write(f"0\nLWPOLYLINE\n8\n{layer}\n90\n4\n70\n1\n")
            f.write(f"10\n{x}\n20\n{y}\n")
            f.write(f"10\n{x+w}\n20\n{y}\n")
            f.write(f"10\n{x+w}\n20\n{y+h}\n")
            f.write(f"10\n{x}\n20\n{y+h}\n")

        # Helper for text
        def text(x, y, content, height=1.5, layer="LABEL"):
            f.write(f"0\nTEXT\n8\n{layer}\n10\n{x}\n20\n{y}\n40\n{height}\n1\n{content}\n")

        # === Geometry (coordinates in µm) ===

        # Input waveguide A (left top)
        line(0, 12, 15, 12)
        line(0, 10, 15, 10)

        # Input waveguide B (left bottom)
        line(0, 4, 15, 4)
        line(0, 2, 15, 2)

        # Taper / merge section
        line(15, 12, 25, 8)
        line(15, 10, 25, 6)
        line(15, 4, 25, 8)
        line(15, 2, 25, 6)

        # Central PTC region (magenta rectangle)
        rect(25, 3, 20, 8, layer="PTC_REGION")

        # Output waveguide
        line(45, 8, 70, 8)
        line(45, 6, 70, 6)

        # Simple hatch suggestion for PTC (small lines)
        for i in range(6):
            line(27 + i*3, 4, 27 + i*3, 10, layer="PTC_REGION")

        # Pump indication (dashed red arrow concept)
        line(30, 14, 40, 14, layer="PUMP")
        line(38, 13, 40, 14, layer="PUMP")
        line(38, 15, 40, 14, layer="PUMP")

        # Labels
        text(2, 13.5, "INPUT A")
        text(2, 0.5, "INPUT B")
        text(30, 12.5, "PTC REGION")
        text(30, 1, "(temporally modulated)")
        text(50, 9.5, "OUTPUT")
        text(32, 15.5, "THz / optical pump")

        # Title
        text(15, 18, "Photonic Time Crystal Logic Gate (schematic)", height=2.0)

        f.write("0\nENDSEC\n")
        f.write("0\nEOF\n")

    print(f"DXF file written: {filename}")
    print("Open it in LibreCAD, FreeCAD, AutoCAD, QCAD, or any DXF-compatible program.")

if __name__ == "__main__":
    write_dxf()
