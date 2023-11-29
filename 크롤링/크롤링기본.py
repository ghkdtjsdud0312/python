from bs4 import BeautifulSoup

#문자열로 간주
# 서버로 부터 가져온 데이터
html = ''' 
<html>
    <table border=1> 
        <tr>
            <td> 항목 </td> 
            <td> 2013 </td> 
            <td> 2014 </td> 
            <td> 2015 </td>
        </tr> 
        <tr>
            <td> 매출액 </td> 
            <td> 100 </td> 
            <td> 200 </td>
            <td> 300 </td>
        </tr> 
    </table>
</html> 
'''
# 크롤링 기본
soup = BeautifulSoup(html, 'html.parser')
print(soup)
result = soup.select('td') # td만 가져옴(tag 선택자와 같음)
print(result)

# 각 태그의 텍스트만 가져오기(배열처럼 돌릴 수 있음)
for val in result:
    print(val.text)