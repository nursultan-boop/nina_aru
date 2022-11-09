# python-flask-nft-metadata

simple flask app which gets nft metadata given the address of nft

# installation

you need to install python 3 https://www.python.org/downloads/

after that install flask using `pip install flask`

next you have to install requests and flask_sqlalchemy

# usage 

1)launch flask web app

2)sign up or login if you already had

![image](https://user-images.githubusercontent.com/60815706/198879333-35cb3aa1-a4f3-4359-95a9-178d1aa9467f.png)

3)provide nft address (you can get it from solanart using the link on that page)

![image](https://user-images.githubusercontent.com/60815706/198879389-dfc63221-6219-424a-a345-bd12079845f2.png)

4)get the results

![image](https://user-images.githubusercontent.com/60815706/198879400-1c4c8112-d76d-43ce-b54c-d1c6de4685b0.png)


# example

enter `3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU` as an adress and get tne following result:

{"mint":"3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU","standard":"metaplex","name":"Baby Yetis #257","symbol":"","metaplex":

{"metadataUri":"https://arweave.net/4PtHGFuAw2U-T4nrIWVRxJ0EpVIivRWi4xjreBkmMVg","updateAuthority":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","sellerFeeBasisPoints":500,"primarySaleHappened":0,

"owners":[{"address":"64eiSEPv2KRKNkPAX6d4BZQ3b12PcFqZP2yPoNAZw9po","verified":0,"share":100},{"address":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","verified":1,"share":0}],"isMutable":true,"masterEdition":false}}
