# Za določen n ∈ N vrne link do n-te strani seznama

def link(n=0):
    domena = "https://gamefaqs.gamespot.com"
    url_razvrščenih_iger = domena + "/games/rankings"  # url brez query parametrov
    query_dodatek = "?page="
    return url_razvrščenih_iger + query_dodatek + str(n)