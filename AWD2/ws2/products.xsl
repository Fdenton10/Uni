<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html> 
            <body>
                <h2>My CD Collection</h2>
                <table border="1">
                    <tr bgcolor="#9acd32">
                        <td style="text-align:left">category:</td>
                        <td><xsl:value-of select="products/product"/></td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

