# -*- coding: utf-8 -*-
import os

with open('/Users/emircanakkale/.gemini/users/user1/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline SVG with clean img tag referencing logo.png with elegant fallback
old_svg_start = content.find('<a href="#" class="brand-logo"')
old_svg_end = content.find('</a>', old_svg_start)

# We want to replace both in navbar and in footer
brand_img_tag = """<a href="#" class="brand-logo" title="NXT - Network X Talent">
        <img src="logo.png" alt="NXT — Network X Talent" class="brand-logo-img" onerror="this.onerror=null; this.parentElement.innerHTML='<span class=\\'logo-fallback\\'>NXT <span>NETWORK X TALENT</span></span>';">
      </a>"""

# Let's inspect CSS for logo
logo_css = """
    /* LOGO STYLES */
    .brand-logo {
      display: flex;
      align-items: center;
      text-decoration: none;
    }
    .brand-logo-img {
      height: 52px;
      width: auto;
      max-width: 220px;
      object-fit: contain;
      display: block;
    }
    .logo-fallback {
      font-size: 1.5rem;
      font-weight: 900;
      color: #FFFFFF;
      letter-spacing: 2px;
      display: inline-flex;
      flex-direction: column;
      line-height: 1;
    }
    .logo-fallback span {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 4px;
      color: #E3E8EE;
      margin-top: 4px;
    }
"""

# Let's write the clean updated index.html with logo.png and form submission hooks
