class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = text.replace( html_sym , formal_sym )
        
        return text
        

s=Solution()
print(s.entityParser(text = "&amp; is an HTML entity but &ambassador; is not."))