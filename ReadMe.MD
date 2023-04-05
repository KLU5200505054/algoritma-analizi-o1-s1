### Alpha-Beta Budama Algoritması
Alpha-beta budama algoritması, minimax algoritmasının geliştirilmiş bir versiyonudur ve genellikle oyun programlamasında kullanılır. Amacı, ağacın daha az düğümünü ziyaret ederek, performansı artırmaktır.

## Algoritma
- Ağacın kök düğümünden başlayın.
- Eğer ağacın derinliği 0'a ulaşırsa veya düğüm bir yaprak düğümü ise, değerlendirme fonksiyonunu kullanarak düğümün değerini hesaplayın ve geri dönün.
- Düğüm, maksimum düğüm ise (yani sıradaki oyuncu maksimizasyon yapacaksa), alpha değerini negatif sonsuz (-∞) olarak ayarlayın ve beta değerini pozitif sonsuz (+∞) olarak ayarlayın.
- Düğüm, minimum düğüm ise (yani sıradaki oyuncu minimizasyon yapacaksa), alpha değerini pozitif sonsuz (+∞) olarak ayarlayın ve beta değerini negatif sonsuz (-∞) olarak ayarlayın.
- Düğümün çocuklarını sırayla ziyaret edin.
- Her bir çocuk düğüm için, alpha-beta budama algoritması tekrarlanır.
- Eğer maksimum düğüm ise, alpha değeri en yüksek çocuk değerine ayarlanır.
- Eğer minimum düğüm ise, beta değeri en düşük çocuk değerine ayarlanır.
- Eğer alpha değeri beta değerinden büyük veya eşitse, düğümün diğer çocuklarına gerek yoktur ve algoritma durdurulabilir.
- Düğümün en iyi değeri, alpha değeri maksimum düğüm için ve beta değeri minimum düğüm için döndürülür.

```
    def alpha_beta_pruning(node, alpha, beta, maximizing_player):
        if node.is_terminal_node():
            return node.get_node_value()

        if maximizing_player:
            v = float("-inf")
            for child_node in node.get_children_nodes():
                v = max(v, alpha_beta_pruning(child_node, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v
        else:
            v = float("inf")
            for child_node in node.get_children_nodes():
                v = min(v, alpha_beta_pruning(child_node, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v
```


Yukarıdaki kod, bir alpha-beta budama algoritmasını uygulayan alpha_beta_pruning() fonksiyonunu tanımlar. Bu fonksiyon, bir node nesnesi verilerek ve alpha ve beta değerleriyle çağrılır. maximizing_player değeri, sıradaki oyuncunun maksimum oyuncu olup olmadığını belirtir.

Bu örnekte, node nesnesi, ağacın bir düğümünü temsil eder ve is_terminal_node() yöntemi, düğümün yaprak düğümü olup olmadığını kontrol eder. get_node_value() yöntemi, düğümün değerini döndürür.

get_children_nodes() yöntemi, düğümün çocuk düğümlerini döndürür. Bu yöntem, düğümün altındaki tüm olası hamleleri hesaplamak için kullanılır. Bu örnekte, node nesnesi, bir oyundaki bir durumu temsil eder ve get_children_nodes() yöntemi, o durumdaki tüm olası hamleleri döndürür.

max() ve min() işlevleri, sırasıyla en büyük ve en küçük değeri döndürür. alpha ve beta değerleri, maksimum veya minimum değerleri izler. Bu değerler, ağaçta düğümler keşfedildikçe güncellenir. alpha değeri, sıradaki oyuncunun maksimum değerini tutar ve beta değeri, sıradaki oyuncunun minimum değerini tutar.

Algoritma, alpha değeri beta değerinden büyük veya eşit olduğunda durdurulur, çünkü bu durumda diğer düğümlere gerek yoktur.


## Zaman karmaşıklığı

Alpha-beta budama algoritması, bir ağacı gezerek en iyi hamleyi belirlemeye çalışırken bazı dalları keserek zaman kazandırır. Bu nedenle, zaman karmaşıklığı ağacın şekline, büyüklüğüne ve hangi dalların kesilebildiğine bağlıdır. Worst-case, base-case ve average-case durumları ayrı ayrı ele alarak, zaman karmaşıklığını hesaplayabiliriz:

Worst-case durumu, ağacın tamamen dengeli olduğu durumdur. Bu durumda, her bir düğümün altındaki tüm düğümler keşfedilir ve tüm dallar kesilemez. Bu durumda, zaman karmaşıklığı, ağacın yapısına ve derinliğine bağlı olarak, O(b^d) olabilir. Burada, b, dalların ortalama sayısıdır ve d, ağacın derinliğidir.

Base-case durumu, ağacın yalnızca kök düğümünden oluştuğu durumdur. Bu durumda, zaman karmaşıklığı sabittir ve O(1) olarak hesaplanır.

Average-case durumu, ağacın rastgele şekilde oluşturulduğu ve dalların kesilebilme ihtimalinin olduğu durumdur. Bu durumda, zaman karmaşıklığı, ağacın yapısına ve dalların kesilme ihtimaline bağlı olarak, O(b^(d/2)) veya O(b^(d/3)) gibi daha küçük bir sayı olabilir.

Bu nedenle, alpha-beta budama algoritmasının zaman karmaşıklığı, ağacın yapısına ve dalların kesilme ihtimaline bağlı olarak değişebilir. Worst-case durumunda O(b^d), base-case durumunda O(1) ve average-case durumunda O(b^(d/2)) veya O(b^(d/3)) gibi daha küçük bir sayı olabilir.

