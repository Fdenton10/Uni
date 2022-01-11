<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" version="4.0" indent="yes"/>
	<xsl:variable name="space">
		<xsl:text>  </xsl:text>
	</xsl:variable>
	<xsl:template match="/">
		<html>
			<head>
				<title>Patient Record XSL Transformation Example</title>
			</head>
			<body>
				<h3>Patient Record</h3>
				<table border="1" cellpadding="4" cellspacing="0" bordercolor="#cccccc" width="400">
					<tr>
						<td width="100">NHS Number</td>
						<td>
							<xsl:value-of select="patient/@nhs-no"/>
						</td>
					</tr>
					<xsl:apply-templates/>
				</table>
			</body>
		</html>
	</xsl:template>
	<xsl:template match="name">
		<tr>
			<td align="left" valign="top">Name</td>
			<td>
				<xsl:value-of select="./first"/>
				<xsl:value-of select="$space"/>
				<xsl:value-of select=" ./middle"/>
				<xsl:value-of select="$space"/>
				<xsl:value-of select="./last"/>
				<br/>
					Title: <xsl:value-of select="./title"/>
				<br/>
					Previous: <xsl:value-of select="./previous"/>
				<br/>
					Preferred: 
					<b>
					<xsl:value-of select="./preferred"/>
				</b>
			</td>
		</tr>
	</xsl:template>
	<xsl:template match="address">
		<tr>
			<td align="left" valign="top">Address</td>
			<td>
				<xsl:for-each select="street">
					<xsl:if test="node()">
						<xsl:value-of select="."/>
						<br/>
					</xsl:if>
				</xsl:for-each>
				<xsl:value-of select="city"/>
				<br/>
				<xsl:value-of select="county"/>
				<xsl:value-of select="$space"/>
				<xsl:value-of select="postcode"/>
				<br/>
			</td>
		</tr>
	</xsl:template>
	<xsl:template match="tel">
		<tr>
			<td align="left" valign="top">Telephone</td>
			<td>
				<xsl:value-of select="./home"/>
				<br/>
				<xsl:value-of select="./mobile"/>
			</td>
		</tr>
	</xsl:template>
	<xsl:template match="email">
		<tr>
			<td align="left" valign="top">Email</td>
			<td>
				<a>
					<xsl:attribute name="href">mailto:<xsl:value-of select="."/></xsl:attribute>
					<xsl:value-of select="."/>
				</a>
			</td>
		</tr>
	</xsl:template>
	<xsl:template match="//fax">
		<tr>
			<td align="left" valign="top">Fax</td>
			<td>
				<xsl:choose>
					<xsl:when test="not(node())">
						<xsl:text>-</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="."/>
					</xsl:otherwise>
				</xsl:choose>
			</td>
		</tr>
	</xsl:template>
	<!--<xsl:template match="text()"/>-->
</xsl:stylesheet>
