# CS50 學習筆記

# Video
- [x] [2013fall / week5](https://www.youtube.com/watch?v=IEuvKVjw2oM)

---
# 190927 Fri
> [CS50 2013 fall week 5 / mon](https://www.youtube.com/watch?v=IEuvKVjw2oM)

## New Concept Video Guideline
- [x] GDB debugger 1:00
- [x] CGI 7:19
- [x] 0x 16Hexadecimal 13:02
- [x] swap 32:02
- [x] malloc 41:29
- [x] Stack Overflow / memcpy 47:38

## Notes
1. [GDB](#gdb)
2. [Pointers](pointers)
3. [CGI](#cgi)
4. [void](#void)
5. [0x](#0x)
6. [swap](#swap)
7. [malloc](#malloc)
8. [Stack Overflow](#stack-overflow)

### GDB
 - GDB是GNU Debugger的縮寫，是一個基於GNU這個自由的作業系統的標準除錯軟體，可以用於逐行/逐組偵錯，支援偵錯如C,C++這樣的語言。
 - 除了偵錯之外，GDB還有反組譯、反推執行檔原始碼的功能
   * GDB還原執行檔原始碼只能推估出大略的原始碼形式
   * 反組譯: 把機器語言還原成組合語言的過程，組合語言把0和1組成的機器語言轉化成對應的文字形式，好讓人們可以理解與記憶。不同的硬體設計會對應不同的機器語言與組合語言。
   * [常見 GNU Debugger (GDB) 指令介紹](http://blog.ywpu.me/2015/03/126-gnu-debugger-gdb.html)
> Why GDB: 學習除錯長遠而言可以幫助工程師節省時間
###### [Notes🔗](#notes)

### Pointers
> What does the `*` mean?  
  - `char*`: `*` 是一個指針，儲存一個實際在記憶體裡的某個地址。`char*` 表示指向記憶體內的一個字串的第一個位置。
  - `int* tmp`: 宣告一個叫做tmp的指標變數，這個變數的資料型態是int整數，存放一個地址。
  - [C語言: 超好懂的指標，初學者請進～](https://kopu.chat/2017/05/15/c%e8%aa%9e%e8%a8%80-%e8%b6%85%e5%a5%bd%e6%87%82%e7%9a%84%e6%8c%87%e6%a8%99%ef%bc%8c%e5%88%9d%e5%ad%b8%e8%80%85%e8%ab%8b%e9%80%b2%ef%bd%9e/#comment-2589)
###### [Notes🔗](#notes)

### CGI
 - CGI全名是computer-generated imagery，是由電腦生成的虛擬圖像。
 - 另一個CGI指的是common gateway interface，是一種協議，規範動態網頁請求資源的標準流程。user對網路伺服器發出request後，透過cgi協議啟動cgi程式要求資源，再回傳結果到網路伺服器，網路伺服器再返回結果呈現於瀏覽器上。
###### [Notes🔗](#notes)

### void
 - `void` 在C裡面表示一種`無效`/`無意義`的資料型態，因為在某些時候程式不需要回傳值做使用所以被定義出來，如printf。
###### [Notes🔗](#notes)

### 0x
 - 0x 是一種在C語言裡面表現16進位制的代表符號。0是便於系統辨認的標示，x表示16進位制的代號，後面接16進位制的表示法來揭示記憶體的位置。
###### [Notes🔗](#notes)

### swap
```c
void swap(int* a, int* b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```
這段程式說明了利用指標交換ab兩個值的範例。
###### [Notes🔗](#notes)

### malloc
- malloc是一種動態配置記憶體的方法，有時因為不確定何時需要用某變數所以不預先定義好變數，此方法讓使用者可以在變數需要被使用的時候再分配記憶體給這個變數，不需要使用的時候再把空間還給記憶體。
###### [Notes🔗](#notes)

### Stack Overflow
```c
#include <string.h>

void foo(char* bar)
{
    char c[12];
    memcpy(c, bar, strlen(bar));
}

int main(int argc, char* argv[])
{
    foo(argv[1]);
}
```
- stack overflow 其技術上的意義是，程式設計師若忘記設定array的邊界，嚴重會導致相鄰記憶體被覆蓋而使電腦癱瘓。這是最古老的駭客攻擊行為之一。
- `memcpy()`: 這個函式用於複製記憶體的內容，複製指定目標(c)內從其地址第一個位置的值(bar)到固定數值(strlen)的位置
- 更多函數說明可參考:[C語言學習筆記---好用的函式memcpy與memset](https://www.itread01.com/content/1547686993.html)
###### [Notes🔗](#notes)

### Other References
1. [如何使用 GDB Debug](https://www.puritys.me/docs-blog/article-329-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8-GDB-Debug.html)
2. [GNU偵錯器](https://zh.wikipedia.org/wiki/GNU%E4%BE%A6%E9%94%99%E5%99%A8)
3. [反組譯器](https://zh.wikipedia.org/wiki/%E5%8F%8D%E6%B1%87%E7%BC%96%E5%99%A8)
4. [組合語言](https://zh.wikipedia.org/wiki/%E6%B1%87%E7%BC%96%E8%AF%AD%E8%A8%80)
5. [組合語言入門教程](https://www.itread01.com/content/1548607715.html)
###### [Notes🔗](#notes)

