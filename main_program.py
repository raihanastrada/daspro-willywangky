import csv
import os

def clear():
    os.system('cls')


def load():
    sizeus = 200  # ukuran maksimal array user
    sizeelse = 1000  # ukuran maksimal array lain
    Auser = [None for j in range(sizeus)]  # template array user dengan ukuran sizeus
    Aelse1 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse2 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse3 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse4 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse5 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse6 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Filename = [Auser, Aelse1, Aelse2, Aelse3, Aelse4, Aelse5, Aelse6]
    File = ['' for i in range(7)]
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    print()
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.reader(csv_file, delimiter=',')
                j = 0
                for row in read:
                    Filename[i][j]=row
                    j += 1
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return Filename


'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''
def obs(password):
    code = ['gAER9V9m', '5jxUjMe5', '7xKrw5i7', 'syUXWeZQ', 'Uw4AmraE', 'mx8OIWfm', 'wmfQYDHp', 'sUq4c8HX', 'db1FTAjy', '6bBF0oJc', '9UfAUf2F', 'Ozb1rb21', 'zVnqqM0Z', '7B2cTFBX', '1rI3DkkB', 'nWG0ElVd', 'VeKBeyK0', '4JPRErQS', 'cv6AuGCQ', 'uWYnRrgP', '6KXlstg3', 'drUrCEZC', 'UVANpVGw', 'oCE3JO1m', 'ACAreCTI', '3IPmiC3b', 'FDOn2jw9', 'PLxENC0w', 'jTXHXdnO', '3bEijGaT', 'IBZokAMY', 'OTe644Yv', 'Nm0Y6wdU', 'eOpmGBkF', '4jltG3k3', 'TE5QYsmN', 'yugSQv8q', 'KuumENPI', 'CIdCvPn8', 'bCLh1cQn', 'FUQtO6gq', 'qURfr0pd', 'NnJT4t7F', 'AfBJZ4LE', 'snjoHL27', 'DfWDqTIW', '1thCYOmH', '63T0NrPI', 'DW9CJKHb', '4ubEx8f2', 'G66LgpN2', '9ovpCt8P', 'rRPl7cFY', 'CgVKaAh2', 'Axl3LuWp', 'cDtBOO0T', '7VtI2P6z', '36t2cbKg', '2fp61Yrx', 'cZHEHmho', 'qxgzFaQX', 'HRwkh5Qt', '3ZLJHs7k', 'Iskpf9Qr', 'PmT0sFhI', 'PeOzV7uT', 'eUpMcEJ1', 'RqiizLH3', 'r7GvAj0g', 'hAgJQbY8', 'ATEJYKv9', 'Ed1ZH9gW', 'D3iraUM8', '8ohvOuWj', 'IHaFeHJw', 'Cj99V86O', 'NG2tFV0n', 'lTrW0iAC', '7DAf6aCL', 'MvlXo0yk', '5UWqn4RX', 'c9gkmIm8', 'qgz6gVF6', 'JjQmyPc4', 'mMxgP73y', 'tH1UUlvA', 'pd2WsCFe', 'VFrXKRRT', 'Adxy5jBU', 'yGmcvkXz', '9ClewOjR', '5vAa7kmd', 'a3Ki1JWn', 'JlBsfOls', '06W70dOe', 'xOlRIhjJ', 'TEMZzl98', '0VqtwJvt', 'eijxVYCe', 'lSdnaNJ8', 'PrTPq4qv', 'oLYhtSN9', 'Z38ILkaj', 'zJymTn8l', 'xlQszhRF', 'odZ04YMN', '59JBgBuA', 'U0cSohvm', '3qLXIi7m', 'Pd94Kqaq', 'w2SrIEQN', 'cHolCONr', 'ofmJdasn', '8YMz4iT9', 'qnrcfCiv', 'Yed4csNb', '1PxbFoUb', '2pdXAJqh', 'MVIAYW8B', 'EjhzILMv', 'vFfXKJBB', 'lr3dpaTo', 'n1rqUEMM', '3ARFjnzp', 'CZQXYDtS', 'BMROtF8h', 'h0eRhPI6', '2QV1fK6u', 'mpLHl3bl', 'zEAynMgq', 'oqsXfB03', 'MVGvMeEn', 'Xr11HIUX', '1D1DW3UJ', 'iUkPLTAX', 'q1gKgykl', 'eqQ6Rpvi', 'm7hPBgcF', 'HWIJl0pE', 'RuF5Ttja', 'eS5KQNX8', 'A6QRc5VX', 'HmWnTRRg', 'cHQCjAB3', 'RpYxi6VL', 'kMMwy5lt', 'TnlijKX0', 'HQUfcGxl', 'WNMVwlqO', 'Tm2GsqKD', 'T0slkNX7', '0wlft095', 'XHZfUwZG', 'FvVvEyyS', 'snDGQNU7', 'hbA16Itw', 'ip9FZI2i', 'siTeCqy3', 'wRMnUhYa', 'R78Km5m4', 'jjGXMxNd', 'WnxVi4rS', 'J27oBqJJ', 'QuMRqmj3', 'yaLbm1vq', 'qP2VYdL8', 'fxS2xOES', 'GOrPbLuB', 'aFVNHt6M', 'ds6XeCHM', '9bDJNRcI', 'p5Al7cC2', 'sThnIFPu', 'akcPXGU3', 'ZlRm8IlH', 'C6ttc7Om', '5G0vxjNc', 'GZiY4GeT', 'LmHADZEs', '6t38yedl', 'vLiplj8v', 'qcurSPeM', 'kZDyA7kR', 'fwMtw4TG', '5W2DdUNq', 'hHGV2Byi', 'iSSgefu8', 'Tdr6zIG6', 'xX9SVlV1', 'Ll08KMnm', 'A1zQIDvt', 'QxhbSrlD', 'O7LCZO1o', 'sJgVSXgR', 'm4SK2T76', 'AIlvH6pr', 'rxE9xtwl', 'ARknihNr', 'IBHUstqj', '3NKE0tgC', 'ptkZSvP9', 'o0J2IDo5', 'NglChiJx', 'E95kSKFG', 'omOGtuMd', 'WpPvgsHA', 'Ud4Cpp2P', 'IbMAE8af', '1suDRJgL', 'YuPIDKvC', 'o2DZwdOM', 'Fu0toMTi', 'g7wwAJ7y', 'E9A5aoED', 'lOoMF82T', 'XQeEm8Tc', '3JefLJjM', 'bXzp34pn', '8WKINZnu', 'CmLiAouD', 'izCUTYZf', 'lERicIq4', 'jDRtFsxl', 'tzo9Cxqu', 'PJaCQoXY', 'w3iM68Cm', 'tdQ1pfKO', 'UePExpSX', 'sh1aZwvQ', 'LZEUfEDe', 'CsGw4PJk', 'n4UExEK7', 'FsG9TMvy', 'OwVqpCwM', 'XTQKhkHu', 'wKA88Orm', 'oGxWUpCL', 'CBWGLiaT', 'WS7SFIAV', 'LGP0MPPC', 'tflOxtg3', 'ORfdtMVw', 'dD8NBNeO', '8pvbnAfE', 'vyr9Xm9a', 'qOjO6AEu', 'aCqT4xzP', 'uhTO1GZA', 'y0HR5iMo', '2nCqmbYd', 'hRzYVfHD', '7EJM90co', 'DdKKEeWV', 'YeR3XGGQ', 'xBRqBZwr', 'XlFGKDBV', '61NhmeQ6', 'rm8w870e', 'UkTgYrCj', 'Q6hLQS8S', 'iPVNNIXE', '2DYhgv6l', 'CdelVVhb', 'gPWfv7O3', 'NQWB3jRE', 'CbLZkPDg', 'mLikHpCB', 'FC0c5P0Z', 'M9RGdloz', 'jiQETB4L', '2wLT9lcg', 'Cs7CeFR4', 'k7Wc45gn', '2sLviiVy', 'pIeC2DTD', 'UXr3g4fS', 'rzYYv5xU', 'gYTxkSjs', 'p9g3UTbt', 'FTJvXtA5', 'xf6tNyKf', 'PsFsqnYL', 'f6GKwUdU', 'iwfwDzbu', '2aPfXomp', 'HKT08eaj', 'qnGMWCqN', 'WYdDwHfr', '9FTPLQpe', 'nGi7W0vs', 'BROcDgPR', 'Bd2KQzTZ', 'm3Uyf1Ni', 'QakQ8257', 'G562npAm', 'popTQxMJ', 'qmTLF9Ei', 'Y6fGwaFz', 'ylaCrmmi', 'mq9KRwza', '4vAHzcNG', 'oj4nImNw', 'P4uergLl', 'vJ8cELLR', 'Fn6VF1nJ', 'xIxM7l0z', '3wMFNRvQ', 'uwUKlpOL', '5k7PUXpu', 'eaZJVqK7', 'c1I5XaKg', 'M5MIJXbZ', 'Poks7qq0', 'jQwcJq4o', 'bw8kd2OA', 'EUiLrLKV', '9i6pG1OQ', 'sG749aCy', 'DbUsJ6Zy', 'gMzCfJjG', 'wyh1dmV2', 'gpm3Z7Ve', '9WUWKsb6', 'ldbWzx2W', 'YodWgJ08', 'hYZxagHZ', '9xTCEowu', 'yjm7yVoD', 'uxrbwWAI', 'UOHzUPbG', 'fgHx51rV', 'tX2DVZd5', 'PhQHbrVz', 'ybaIqTKF', 'MruVuxGX', 'eGbOCL71', 'xjbyk1q0', 'WsSb5aGW', 'UctMayJq', 'EW7RfZgt', 'DyqXOlJG', 'Jnq1d8sZ', 'NI0lctii', 'pjemuQTk', 'aLTn4Dzq', 'FJ3Ua3FS', '3mJFrhb7', 'ix6Z09mr', 'PY25QLSR', 'aK01rjwO', 'KzkXDogf', 'EFUZOPLM', 'm4X3uVaE', 'RSbKkxei', 'FRlclsto', 'Q8Vmx3SQ', 'hRgAjKr3', 'ZAbGss0o', 'SHbprXus', '6S2KL8To', 'jjatG2Jh', 'B9loGyLp', 'F7NaJzlK', '5fy7rCm6', 'sQwlgGQ7', 'Ma6rFFAn', '1RnYTU5s', 'YgXAv31j', 'lFCcfwSx', 'bHEpBcud', 'NjSyM3fB', 'bKdrdtEZ', 'sAZmkYn3', 'i6DWGBOY', '73tx5GMQ', '14rnobd2', 'Z69IgpCw', 'hrZyhs4v', 'bbPBT6rJ', 'Aa37HS7m', 'LbpsIDaF', 'HHnKpuas', '77ZNsws3', 'prj16sT1', '5A4L1Wq2', 'Ae2WyXN2', 'cp2Ldgr7', 'iDqpAVKw', 'PFxY3l4e', 'qsI5DJCm', '5EFMOQLk', 'S3oEtyiZ', 'VoW9Kgwu', 'ylnVJzA5', 'vArOyy7G', 'lRAgBAsc', 'Om2dxtUT', 'udwbz2hD', '6gOGmW1V', 'N7nmjTMQ', 'p5WX18yH', 'Cn41JW3g', 'BRV9praP', '8eSbITZa', 'aNrWfrAi', 'jHZQ6ZiY', 'fjmUK1ux', 'SVCte5LC', 'rd9c2itw', 'JntEg5a1', 'tZ81Clxk', '2PNS5sg0', 'Y4TLHKOH', '9KJT63Uu', 'SDiI7nwF', 'W7UeYzTc', 'PvTXbkqk', 'OD9GwYAV', 'u9GdMSr8', 'xihKbGZ0', 'aEMW5hPk', 'e6ErzQrV', 'jXXXIbSB', 'GxnUt2CR', 'Fwrfcz0P', 'fjfKD2KV', 'SXpOpRuT', 'iZOVXJd3', 'xSSneCtt', 'MSGYdCZV', '3KWs2upY', 'qXvIoPkc', 'Fp5jSA7n', 'C0Et17Zo', '2H1eBo7I', 'yHCcjhtb', 'aFs7loYE', 'kPo6WoFE', 'PdOBGphT', 'T3Kjbw6H', 'h6CpUPHT', 'hA0fYphX', 'l2SlFVHU', 'ZzXqPKbK', '6Zm0aQCH', 'WmbNdr7X', 'l8WUP1vf', '11W1CXZq', 'zr7hO5KE', 'SNUcEpqb', 'e9aTx5j7', '4aXOc8dL', 'MR7Q4ro5', '6mhu5QQL', 'k2o1LL6W', 'YNtF1jA5', 'DMOUTaeB', 'C3U8qUDb', 'KYJfILKU', 'gbXJIv9j', 'Rtcz7fAI', '4YieU3ix', 'oU0rtrrr', 'zA1EXGDi', '2mLTcKrc', 'r8NdUKhs', 'mMmQHauR', 'i2xCg0Ky', '7d9qEsfI', 'PAJOUw6O', 'Usoc5A5J', '2gFnqEUW', 'OGcGShDh', '6pHd4KOs', 'oFLCFD7O', 'eqfzSzTC', '5hx64G0Q', '3mG22v16', 'tHRMiGcU', '6d0hcfId', '9v6G41ZE', '2HcNUVxG', 'yejTRPFK', 'MeyoF1nP', 'bbE5brAK', 'FScxWtwW', 'hGFcSxIW', 'lhFDqYGx', 'YB9Kmrzy', 'R1Ma0dCu', '1okiyyaP', 'hIG6JwUk', 'pPDGqC0c', 'uMorZNdD', '0XpiqEFL', 'bU5mgZjY', 'mGtCrdhd', 'PMHXIedu', 'q0wUk8GB', 'cb9cibRe', 'WJIjZLVM', 'VQojryoD', 'Bg4XqXdr', 'ZvgfG6ml', '4Z21XkOI', 'TVZsmRom', 'BGKo8x8u', 'KXbmJSZi', 'BEd93i4H', 'zMDPWF27', '4UaCSWL3', 'sFqOTNBw', 'agpdOQ9o', 'B1TXTX2V', 'vW7KjCba', 'rFmt5mGi', 'uObSJWkv', 'YBc6EYdU', 'VbKYQal4', '9kK1WRxr', 'Q0g9mYwU', 'iULO9v8N', 'P6AWbMdO', 'PYIXUIFv', 'DKVNJTxi', 'oZbZtuTG', '0A0eXKPW', '3BK2APhe', 'tbw0GKkp', 'Ojujc9Dq', '1TpKuf6v', '9b65XBiw', '9vmPBZE8', 'XFJsu5jH', 'gkrrFBLb', 'VkjzPdR9', 'GTUBhuqa', '67CpM1OG', 'K4rB2ift', '9H2ymsXt', 'Yv3L6xn2', 'N0NPGPeW', 'xe9IMgez', 'cYZ19rXC', '2J0unRGG', 'cFUs1YBG', 'S1gC8KAM', '7HGRvalE', '0HDWFpHH', 'qDgiXClI', 'Fgj5CAAs', 'FZLQP190', 'IgQkX8Gi', 'wYYa3X7R', 'AlwlG2qQ', 'aLiqUeBr', 'EDWeoCan', '5TU6Makh', 'yo9okxhI', 'L9KNLQzN', '0Mx0BjfH', 'QmUZpzFa', 'Nbw56vpl', 'Dt17TPbg', 'BPUEdgns', 'fmPLorGZ', 'oDaDbKm1', 'puDIVHSZ', 'QWvSSqJC', 'AT324pNp', '4WQGH2Dn', 'cTfZoMQW', 'nKkVxPTC', 'J5i8SOlA', 'IHqHIJjf', 'dKxkn12u', 'ykrEXLRp', 'CeIIq0rj', 'HtI5DtS1', 'idLgMwlo', 'bnVEVGLz', 'gjTfUWeE', 'TwojqpFV', 'uS3HEI3B', 'v6qVs44D', 'oL5Ha9uh', 'CmCV3iCE', 'Tm0hRFOk', 'ntloWNZW', 'whHvzv82', 'kUmIY0s6', 'ANS3OVJT', 'nsyR3n4U', '0MLqXOYb', 'rpGq5spO', 'NJA6uM1t', 'tASEAJVH', 'JAa6cQpu', '61TwqoHM', 'vChglIqC', 'IY0vntfG', 'Ks6FrjJ0', 'x2l1F2y6', 'Qn1LwnF0', 'LXsEqCot', 'EMN9Paws', 'tu1calKk', 'CYEM9hYc', 'mw0H0wBo', 'tYiuYai6', 'Q14nii7u', 'IwBN0tVP', 'cpEF47DC', 'PGADj3u7', 'f7teni16', 'Ij8II3AM', 'mgyMc3I4', 'DuhGvH09', '12BOKBjp', '6pv8m0Ur', 'ORNEMbDl', 'HAE2fuw6', 'gFCXSogJ', 'h6C0NzTW', 'mmaZlxZo', 'J33bTrIC', 'azLH3lBs', 'nV8UM2LE', 'DLvndSa6', 'rjef5Nax', 'kLfSrz2y', 'P53UEDej', 'Ke06EbLU', 'ykcp97Ye', 'vrIPQKsv', 'VvflKVrK', 'kVheRMtU', 'LWKBDwT2', 'hGcUmF1m', 'CHtte3JK', 'koOZhQ9V', 'vyWGaUWr', 'o76Sg2yU', 'HA4Vxjd3', 'Jk8BCpwz', 'qvXj1p3N', 'NjrFINhB', '6G3MfR36', 'fHxLhLMG', 'Kt1M5c1h', 'OBWTDJsD', 'ZMQCIUjz', '76SuydOc', 'FMVTtARz', 'd9s8qzbD', 'KY8tFzxH', 'A043pqKo', 'pnoM86DT', 'AiP84SlH', 'DB06jPrC', 'aWScFcFu', 'l5LjKb15', '5r5Wa0vf', 'g2aiMdVT', 'oqr80iLu', 'c8lnQ7aP', 'uxZazz3y', 'M0Kw1ppP', 'EwRDDjWr', 'EVXOhMBy', 'rvCoyJCZ', '3vZKHlEQ', 'Xn5hIP0e', 'LrUd8Kpr', '5cFKpBLf', 'wsn2zgq4', 'SupvOFsW', 'GvwnrwiE', '24JsSUuS', 'Jv3rLiYJ', 'cdLZkVC8', 'ZZ5PdAn8', '146NbkJl', '8b1KYreV', 'QQQQbsiV', 'szFYJxI5', 'GS3p8ps5', 'KdGbk0LL', 'UQFj1Dh5', 'vsvjRbgP', 'pAH1jmru', '7pf47CtN', 'FAsBiglL', 'ZMo8E5jf', 'WQEMEMBP', '1Fe3v12O', 'LhX70OcH', 'Wsl9jJ1o', 'dSrJq3rY', 'p9iRafVd', '7kITjRmC', 'pwktAGxZ', 'T3ksrLTz', 'wGmr85Xl', 'nSeoHur4', 'jLdUgPJD', 'ZtKMdkk9', 'hO318Dkb', '1ehVR43V', 'bBMsURcG', 'bPbi2jOi', 'lrBuF0vl', 'xN3rykvB', 'TQZayvgW', 'KaJkQ5gZ', '6Id7nOJr', 'm3bk9GGF', 'jRMfaZYc', 'zsj6bDVa', 'Qrj1AtmX', 'XLlxCUi3', 'tTdOjATm', 'SySTor0r', 'RVyHbJIf', '2RlueG4h', 't7BnjlVQ', 'tyNKqADa', 'okNekXLB', 'ONvHcruv', 'zg7MAoIm', '7zz7joYx', '6f5nUHGP', 'qXJ5jtGd', 't9P4SDJS', 'HqaTQOLx', '8e3slcf7', '7LFV3tES', 'vn8D2tQa', 'l9Bh3QnH', 'qYED8RU0', 'zQAqiHkH', 'Hnl5m5fv', 'HR8IdxOT', 'kxW0RBVU', 'oq1wfuoy', 'fkAHxdBL', 'XEgPrjtm', 'UyxIFAZg', 'SD8EmPP6', 'CcWOfYGP', 'Tm4Zxv9F', 'iG8TwoY2', 'WYByHLRK', '8oWfPSTz', 'dEWCOd4P', 'Dmye9lNQ', 'o2xvJjvM', 'igX8a80s', 'ZAeA16Ps', 'UJsk82Dj', 'mVW06Q8M', 'MfWxs2VJ', '1p7ADpk8', 'Lv1x1Fse', 'aKlH1oze', 'VBBf6oVw', 'U5vcczAD', 'K18uGT3a', 'DrIIatPb', '00rmTzdf', 'sfDeFXTj', 'FEGIXcgt', '9t1c1yMR', 'YluUmuwA', 'BDl13AQV', '0MfJxY5W', 'XN66xcFK', 'iH1xuUPK', 'DZKK2zaG', 'IPb6gyiS', 'E1zi4p9g', 'WXHfOzQq', 'W3Y98RCW', 'm8KeWmo6', 'Bw8TVOlX', 'A8BBRAlI', 'ECsMNbZS', '1jibt170', 'v9G5JVnL', 'TrpjBpWo', 'YUkg1dG1', 'Vdw85Hvx', '2Y4CPw0A', 'zKt6y4aG', 'VHxl0jPB', 'SWKv39p7', 'zD7hHj4l', 'CPLZA1LL', 'oeLUy5qa', '733bHhS3', 'gwe3YWGa', 'rXlI0FMp', 'Ly3OPJKP', 'ivdG80h0', 'aiyu26dz', 'Sf6TqEIO', 'b1qNX1uB', 'AjjTjP7k', 'hnglSEKz', 'YeRv5m9j', 'ILoGfKcw', '0ZQAe8YI', 'zjgLg9b3', 'eWVg65Ab', 'Nwxii86I', 'xa4J4eLX', 'rWVJv3yt', 'IlwEYLaO', 'IoLeXlIV', 'kmq3IA0m', 'MXrm0UZh', '5rugTB5q', '5GezwxHD', 'atXmt6qm', '0YkTGYDx', 'ALLKgr0s', 'CVXzymit', 'V9cXxK1j', 'q2TCxmn3', 'OB6F5vk1', 'Xo88EEan', 'PV3NTPVu', 'z2tGbfdn', 'QFu3JUTY', 'Hqr77F5A', '7T5hu8R8', 'Eis7dcKX', 'lwF1Qoxa', 'uZiWypIw', '8D3r2GxC', '5LigHFxV', 'ULGwIxNX', 'BH53lDD5', 'dS0qk1Zh', '5rfWWQun', 'VbuPhPxt', '8H7sCl4R', 'pJulBlzJ', 'Y3tUuND9', 'hzOhzDPk', '8iNdaJTX', 'gN4TdL7J', '5TCi1E0T', 'K4dKtauP', '1VRKi7eg', 'mYQUXvHo', 'qxVxmBeK', 'FIAqBjpH', 'yTTCY2LX', 'PM9yydVf', 'nyQ6tCS5', 'HuksZLB0', '3j7rL9OC', 'WktkLDzr', 'ruGX5zz4', 'APBwtSuy', '0pN9ZZ9f', 'jOkrHjGz', 'oAOsEVFf', 'E0Gk6LCG', 'EmprrzZe', 'RYaZXXFh', 'Y3CXImEG', '5WBM8vIf', 'XYc34yYB', 'uUT79cLq', 'abd8Nr3v', 'PKsmOoyt', 'UVTxpNAr', 'vjZUXsQZ', 'onjt6Zbk', 'GbcuA3oT', 'Yl302LtJ', '0XhZuaWQ', 'BJUpgOk1', 'NwRRcPoJ', 'q96eUc4b', 'i9OTZW4f', 'p6uS3pK3', 'SvezPhY5', 'AVl2UNzb', 'vMueZqLi', 'qLFaPFS2', 'XDOXwC0K', 'yjHrAlfu', 'gOoiEAgS', '29BN6jxA', 'Hj3ddAc4', 'm07KtudD', 'RkCDxC1Y', 'wYOWnsQ8', 'QlAEowtO', 'hahOZS2v', 'vpf1Xp9M', 'SyFCziR1', 'vlWNMCcB', 'Yro1JMwQ', 'Q1BRLeQB', 'N0M6s3JB', 'ojxqRIpG', 'rm41G3LH', 'Wv5CzcYh', '4q8UPXTV', 'ZWO1cgg6', '1IzRN4u9', 'dIlMLs3r', 'ywb553FS', 'ixfM1Xmy', 'YSMsxf2f', 'Ei9Out6O', 'qCahzvTn', '9Sy6mIz8', 'KWe6BSWd', 'zQUogQYN', '9VClA4D8', 'ZhDi7HLu', 'FsEq9jfc', 'fSoMHN14', 'v53q3coM', 'XrUxfMUf', 'uzineSPi', 'OKVtUor9', 'Fr41dxDr', 'tlG2h826', 'IaEYBFFX', 'MXt6Ge1B', 'd8L4TY7D', 'ruIp6pvO', 'ZIQXRkqO', '8huiUURD', 'qYNXhRXM', '4XrINJ88', 'jhhrKdl9', 'XJUWNH5P', '3n0a5Cat', 'vtu1VK0B', 'bDIDlVPv', '0iHylKeq', 'iZL6qcGB', 'TZsxPbg8', 'WH7X4Hlo', 'Z6q8vtn1', 'ACq3NHb7', 'zSaR8ToC', 'zPL0vrXg', 'MP3fvy5y', 'IHL29f9g', 'Z1tJn4pc', 'XGXxnBFU', 'lSS907F9', 'UJdYeV1l', 'tL20AK7w', 'hlay9xvH', 'IwVItrvd', 'Rs0oGi2s', 'WSR3QLTC', '90QJ1tbn', 'Ks3mgz4B', 'SWjEl5Xa', 'dfVYvSN4', 'wZAbaBhZ', 'lCGouZRc', '3na7lDhX', 'hFgQTRB2', 'IJLuUUhn', 'q1QDNtKb', 'xhAMaj2n', 'rJfcLjMH', 'ORIVJ7EI', 'NSquJvHL', '6nL0Cq4G', 'RPkKobHk', 'sCPn6Fcq', 'eXS3EnBC', 'BNsk9DfJ', 'bBljklYp', 'q7bNXqPs', 'aebRpbD4', 'ERlEvpyB', 'qYTQGQev', 'BMIGuhyE', '5EaFl8or', '75xUmkfY', 'fe4EGEvk', 'DEYJISzK', '6xehthj7', 'E66NZt08', 'JhFrBgfx', '4VaQ1omf', 'ekgcr1xE', 'eFuI3OVX']
    hiddenpw = ''
    i = 0
    valid = True
    while valid:
        try:
            hiddenpw += code[ord(password[i])] # enkripsi disesuaikan dengan ordinat per karakter
            i += 1
        except:
            valid = False
    return hiddenpw


def login():
    login = False
    while (not login):
        un = input("Masukkan username: ")
        pw = obs(input("Masukkan password: "))
        print()
        i = 0
        while True:
            if (Filename[0][i] != None): # Mengecek apakah username dan password sesuai di File user
                if (Filename[0][i][3]==un and Filename[0][i][4]==pw):
                    login = True
                    break
                i += 1
            else:
                break
        if (login == True):
            print("Selamat bermain,",un,"!")
        else: # Pesan kesalahan akan muncul bila salah login
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    if (un=="ADMIN"): # Akan mendeteksi admin
        admin = True
    else:
        admin = False
    birth = Filename[0][i][1] # Meminta tanggal lahir
    height = Filename[0][i][2] # Meminta tinggi badan
    role = Filename[0][i][5] # Meminta jenis pemain
    print()
    return admin,un,birth,height,role

def signup():
    # Local Function
    def ucheck(a,b): # Bila username telah terdaftar, maka Exist = True
        Exist = False
        i = 1
        while (b[i] != None):
            try:
                if b[i][3] == a:
                    Exist = True
                    break
            except:
                Exist = False
            i += 1
        return Exist

    # Function Algorithm
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
    Username = input("Masukkan username pemain: ")
    while (ucheck(Username,Filename[0]) == True): # Bila Exist = True, maka akan meminta ulang input username
        print("Username sudah terdaftar")
        Username = input("Masukkan username pemain: ")
    Password = input("Masukkan password pemain: ")
    print()
    i = 0
    while True:
        if (Filename[0][i] == None): # File user
            Filename[0][i] = [Nama, Tanggal_Lahir,Tinggi_Badan,Username,obs(Password),'Pemain',0]
            break
        i += 1
    print("Selamat menjadi pemain, {}. Selamat bermain.".format(Nama))
    return Filename


def cari_pemain():
    found = False
    un_search = input("Masukkan username: ")
    print()
    if (un_search != "ADMIN"): # Tidak bisa mencari ADMIN
        i = 0
        while (Filename[0][i] != None):
            if (Filename[0][i][3]==un_search): # Keterangan pemain akan ditampilkan di sini
                print("Nama Pemain: ",Filename[0][i][0]) # File user . nama
                print("Tinggi Pemain: ",Filename[0][i][2]) # File user . tinggi
                print("Tanggal Lahir Pemain: ",Filename[0][i][1]) #File user. tanggal lahir
                found = True
                break
            i += 1 
    if (not found):
        print("Pemain tidak ditemukan")
        

def tambah_wahana():
    id = input("Masukkan ID Wahana: ") # NNNAAA (3 angka dan 3 huruf)
    nama = input("Masukkan Nama Wahana: ")
    harga = input("Masukkan Harga Tiket: ")
    umur = input("Batasan Umur: ") # dewasa, anak-anak, semua umur
    tinggi = input("Batasan Tinggi Badan: ") # >=170 , tanpa batasan
    print()
    wahana = [id,nama,harga,umur,tinggi]
    i = 0
    while True:
        if (Filename[1][i] == None): # akan mengisi array kosong
            Filename[1][i] = wahana
            break
        i += 1
    print("Info wahana telah ditambahkan!")
    return Filename

def riwayat_wahana():
    ID = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    count = 0
    i = 0
    while (Filename[3][i] != None): # Mengecek File wahana
        if (Filename[3][i][2]==ID):
            tanggal = Filename[3][i][1]
            user = Filename[3][i][0]
            tiket = Filename[3][i][3]
            print("{} | {} | {}".format(tanggal,user,tiket))
            count += 1
        i += 1
    if (count == 0): # Memunculkan pesan bila tidak ditemukan riwayat
        print()
        print("Riwayat tidak ditemukan")

def cari_wahana():
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()
    # Input akan divalidasi terlebih dahulu
    while True:
        jenis_umur = int(input("Batasan umur pemain: "))
        if (jenis_umur == 1 or jenis_umur == 2 or jenis_umur == 3):
            break
        else:
            print("Batasan umur tidak valid!")
    while True:
        jenis_tinggi = int(input("Batasan tinggi badan: "))
        if (jenis_tinggi == 1 or jenis_tinggi == 2):
            break
        else:
            print("Batasan tinggi tidak valid!")
    
    # input akan disesuaikan dengan format pada file
    if (jenis_umur == 1):
        jenis_umur = "anak-anak"
    elif (jenis_umur == 2):
        jenis_umur = "dewasa"
    elif (jenis_umur == 3):
        jenis_umur = "semua umur"
    if (jenis_tinggi == 1):
        jenis_tinggi = ">=170"
    elif (jenis_tinggi == 2):
        jenis_tinggi = "tanpa batasan"
    
    count = 0
    print()
    print("Hasil Pencarian:")
    i = 0
    while True: # Setiap wahana yang cocok akan ditampilkan
        if (Filename[1][i] != None):
            if (Filename[1][i][3]==jenis_umur and Filename[1][i][4]==jenis_tinggi):
                print("{} | {} | {}".format(Filename[1][i][0],Filename[1][i][1],Filename[1][i][2]))
                count += 1
            i+=1
        else:
            break

    if (count==0): # Akan muncul pemberitahuan bila tidak ada wahana terkait
        print("Maaf, wahana tidak ditemukan")


def lihat_laporan():
    if (Filename[6][1]==None): # Akan muncul pesan bila tidak ada laporan
        print("Tidak terdapat kritik dan saran") 
    
    else :
        count = 0
        while (Filename[6][count] != None): # Menghitung banyaknya baris file laporan
            count += 1
        for i1 in range(1,count-1): # Mengurutkan laporan secara alfabetis
            for i2 in range(i1+1,count):
                if (ord(Filename[6][i1][2][0]) > ord(Filename[6][i2][2][0])):
                    temp = Filename[6][i2]
                    Filename[6][i2] = Filename[6][i1]
                    Filename[6][i1] = temp
                elif (ord(Filename[6][i1][2][0]) == ord(Filename[6][i2][2][0])):
                    if (ord(Filename[6][i1][2][1]) > ord(Filename[6][i2][2][1])):
                        temp = Filename[6][i2]
                        Filename[6][i2] = Filename[6][i1]
                        Filename[6][i1] = temp
                    elif (ord(Filename[6][i1][2][1]) == ord(Filename[6][i2][2][1])):
                        if (ord(Filename[6][i1][2][2]) > ord(Filename[6][i2][2][2])):
                            temp = Filename[6][i2]
                            Filename[6][i2] = Filename[6][i1]
                            Filename[6][i1] = temp
                        elif (ord(Filename[6][i1][2][2]) == ord(Filename[6][i2][2][2])):
                            continue

        j = 1
        while (Filename[6][j] != None): # Menuliskan laporan yang telah diurutkan
            print("{} | {} | {} | {}".format(Filename[6][j][2],Filename[6][j][1],Filename[6][j][0],Filename[6][j][3]))
            j += 1


def topup():
    found = False
    while (not found): # Akan terus mengulang bila data yang dimasukkan salah
        un = input("Masukkan username: ")
        saldo = int(input("Masukkan saldo yang di top-up: "))
        print()
        i = 0
        while (Filename[0][i] != None):
            if (Filename[0][i][3] == un): # Mengecek username di file user
                nama = Filename[0][i][0]
                Filename[0][i][6] = int(Filename[0][i][6]) + saldo  # Menambahkan saldo sebelumnya
                found = True
                # Akan muncul total saldo setelah pengisian
                print("Top-up berhasil. Saldo {} bertambah menjadi Rp{},00".format(nama,Filename[0][i][6]))
                break
            i += 1

        if (not found): # Akan muncul pesan kesalahan
            print("Data yang anda masukkan salah! Silakan masukkan ulang.")
    return Filename

def jumlah_tiket():
    username = input("Masukkan username: ")
    print("Riwayat:")
    i = 0
    found = False
    while (Filename[4][i] != None): # Mengecek file kepemilikan tiket
        if (Filename[4][i][0] == username): # Username akan dicocokkan
            ID = Filename[4][i][1]
            j = 0
            while (Filename[1][j] != None): # Mengambil nama wahana dari file wahana
                if (ID == Filename[1][j][0]):
                    wahana = Filename[1][j][1]
                    break
                j += 1
            jumlah = Filename[4][i][2]
            print("{} | {} | {}".format(ID,wahana,jumlah)) # Muncul jumlah tiket per wahana
            found = True
        i += 1
    if (not found): #Data kosong, maka akan muncul pesan
        print()
        print("Data tidak ditemukan!")


def kritik_saran(un):
    # Proses memasukkan kritik dan saran (Asumsi masukan valid)
    ID_Wahana = input("Masukkan ID Wahana: ")
    Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
    Username = un #un = username awal, di login
    Isi_Kritik = input("Kritik/saran Anda: ")

    i = 0
    while True:
        if (Filename[6][i] == None):
            Filename[6][i] = [Username,Tanggal_Kritik,ID_Wahana,Isi_Kritik]
            break
        i += 1
    print()
    print("Kritik dan saran Anda kami terima.") # Pesan berhasilnya menerima laporan
    return Filename


## ALGORITMA UNTUK BELI TIKET
def umurvalid(now, birth):  # Fungsi untuk menghitung umur user
    hari_lahir = int(birth[0:2])
    bulan_lahir = int(birth[3:5])
    tahun_lahir = int(birth[6:10])
    hari_now = int(now[0:2])
    bulan_now = int(now[3:5])
    tahun_now = int(now[6:10])
    if (tahun_now - tahun_lahir) > 17:
        dewasa = True
    else: # tahun_now - tahun_lahir <= 17
        if (tahun_now - tahun_lahir == 17):
            if (bulan_lahir > bulan_now):
                dewasa = True
            elif (bulan_lahir == bulan_now):
                if (hari_lahir >= hari_now):
                    dewasa = True
                else:
                    dewasa = False
            else:
                dewasa = False
        else:
            dewasa = False
    if (dewasa):
        return 'dewasa' # anggapan lebih tua dari batas umur 17
    else:
        return "anak-anak" # umur < 17 tahun

def beli_tiket(username,user_birth,user_height,role): #parameter dari login
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang dibeli: "))
    arrUser = Filename[0] # Mengecek file user
    arrWahana = Filename[1] # Mengecek file wahana
    arrBeli = Filename[2] # Mengecek file pembelian
    arrTiket = Filename[4] # Mengecek file kepemilikan tiket
    i = 0
    found = False
    while (not found and arrWahana[i] != None): # Mengecek apakah wahana terkait ada
        if (arrWahana[i][0] == wahana): # mengambil nomor baris pada file wahana
            wahana_id = i
            found = True
            if (role == "Pemain"): # harga normal untuk status pemain biasa
                harga_tiket = jml_tiket * int(arrWahana[wahana_id][2])
            elif (role == "Golden"): # setengah harga untuk status golden
                harga_tiket = jml_tiket * int(arrWahana[wahana_id][2]) / 2
            break
        else:
            i = i + 1 
    if (arrWahana[wahana_id][4] == "tanpa batasan"):
        batas_tinggi = 0
    else: # >=170
        batas_tinggi = 170
    if (found) : # Bila wahana ada, akan dicek apakah umur dan tinggi pemain sesuai
        if ((umurvalid(str(tanggal), str(user_birth)) == str(arrWahana[wahana_id][3]) or str(arrWahana[wahana_id][3]) == "semua umur") and int(user_height) >= int(batas_tinggi)):
            j = 0
            valid = False
            valid_saldo = False
            while (arrUser[j] != None):
                if (arrUser[j][3] == username):
                    if (int(harga_tiket) <= int(arrUser[j][6])): # Mengecek apakah saldo cukup
                        valid_saldo = True
                        i = 0
                        while True: # jumlah baris pada array
                            if (arrBeli[i] == None): # mengecek baris kosong awal dari array yang sudah tersedia
                                arrBeli[i] = [username, tanggal, wahana, jml_tiket] # mengisi baris kosong dengan data yang diinput
                                break
                            i += 1
                        arrUser[j][6] = int(arrUser[j][6]) - harga_tiket # mengurangi nilai saldo pada array user
                        i = 0
                        while True: # melihat array file kepemilikan tiket
                            if (arrTiket[i] == None): # mengecek apakah user sudah memiliki tiket di wahana tsb
                                arrTiket[i] = [username, wahana, jml_tiket]
                                break
                            else:
                                if (arrTiket[i][0] == username and arrTiket[i][1] == wahana): # mengecek apakah user sudah punya tiket
                                    arrTiket[i][2] = int(arrTiket[i][2]) + jml_tiket # menambahkan jumlah tiket ke file yang sudah ada
                                    break
                            i += 1
                        nama_wahana = Filename[1][wahana_id][1]
                        print("Selamat bersenang-senang di {}.".format(nama_wahana))
                        break
                    else:
                        print("Saldo Anda tidak cukup")
                        print("Silakan mengisi saldo Anda")
                j += 1

        else: # Muncul pesan bila belum memenuhi persyaratan tinggi dan umur
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")

        Filename[0] = arrUser
        Filename[1] = arrWahana
        Filename[2] = arrBeli
        Filename[4] = arrTiket

    else: # Muncul pesan bila ID yang dimasukkan tidak ada
        print("Wahana tidak ditemukan!")

    return Filename


def pakai_tiket(username):
    arrTiket = Filename[4] # Mengecek file kepemilikan tiket
    arrPenggunaan = Filename[3] # Mengecek file penggunaan tiket
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang digunakan: "))
    print()
    valid = False
    i = 0
    while (not valid): # searching kepemilikan tiket dari user
        if (arrTiket[i] != None):
            if (arrTiket[i][0] == username and arrTiket[i][1] == wahana):  # Menghitung apakah tiket cukup
                if (int(arrTiket[i][2]) >= jml_tiket):
                    valid = True
                    arrTiket[i][2] = int(arrTiket[i][2]) - jml_tiket # mengurangi jumlah tiket pada array kepemilikan
                    break
                else: # Pesan bila tiket tidak cukup
                    print("Maaf tiket anda kurang! Silakan membeli tiket lagi.")
                    break
            else:
                i += 1 # next element
        if (arrTiket[i] == None):
            break
    if valid: # jika user memiliki tiket yang cukup
        print("Terima kasih telah bermain.")
        i = 0
        while True:
            if (arrPenggunaan[i][0] == username and arrPenggunaan[i][1] == tanggal and arrPenggunaan[i][2] == wahana):
                arrPenggunaan[i][3] += jml_tiket
                break
            elif (arrPenggunaan[i] == None): # Riwayat bermain disimpan ke file penggunaan tiket
                arrPenggunaan[i] = [username, tanggal, wahana, jml_tiket] # menambahkan data ke file penggunaan tiket
                break
            i += 1
    else: # Pesan bila masukan tidak valid
        print("Tiket Anda tidak valid dalam sistem kami")
    Filename[4] = arrTiket
    Filename[3] = arrPenggunaan
    return Filename


def refund(username,role):
    id = input("Masukkan ID Wahana: ")
    tanggal = input("Masukkan tanggal refund: ") # now = masukkan tanggal saat ini
    tiket = int(input("Jumlah tiket yang ingin di-refund: "))
    print()
    found = False
    i1 = 0
    
    while (Filename[4][i1] != None): 
        if (Filename[4][i1][0] == username) and (Filename[4][i1][1] == id): # Mencari apakah pengguna memasukkan input yang valid di tiket.csv
            if (int(Filename[4][i1][2]) < tiket):
                break
            else :
                found = True
                Filename[4][i1][2] = int(Filename[4][i1][2]) - tiket # jml tiket di tiket.csv dikurangin

                i2 = 0
                while (Filename[1][i2] != None): # pencarian harga tiket suatu wahana untuk penghitungan refund
                    if (Filename[1][i2][0] == id) :
                        if (role == "Pemain"):
                            refunds = 0.75*(int(Filename[1][i2][2]))*tiket # kembalian 75% harga untuk pemain biasa
                        elif (role == "Golden"): # kembalian 75% dari setengah harga untuk pemain golden
                            refunds = 0.75*(int(Filename[1][i2][2]))*tiket/2
                        break
                    i2 += 1

                i3 = 0   
                while (Filename[0][i3] != None): # pencarian username di user csv untuk penambahan saldo
                    if (Filename[0][i3][3] == username):
                        Filename[0][i3][6] = int(Filename[0][i3][6]) + refunds # penambahan saldo di user.csv 
                        break
                    i3 += 1

                # pencatatan di refund.csv
                temp = [un,tanggal,id,tiket]
                i = 0
                while True:
                    if (Filename[5][i] == None):
                        Filename[5][i] = temp #penulisan di array
                        break
                    i += 1
            break
        i1 += 1

    if (found == True): # Pesan bila refund berhasil
        print("Uang refund sudah kami berikan pada akun Anda.")
    else: # Pesan bila masukan tidak valid
        print("Anda tidak memiliki tiket terkait.")

    return Filename

def save(): # Tidak ada pengulangan karena asumsi semua masukan valid
    File = ['' for i in range(7)] # Meminta kembali file yang ingin disimpan
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Name = ['User: ','Daftar Wahana: ','Pembelian Tiket: ','Penggunaan Tiket: ','Kepemilikan Tiket: ','Refund Tiket: ','Kritik dan Saran: ']
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            open(File[i])
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
            while (Error[i] == True):
                File[i] = input('Masukkan nama File ' + Name[i])
                Error[i] = False
                try:
                    open(File[i])
                except:
                    Error[i] == True
    if (Error.count(True) == 0): #Pesan kesalahan bila file tidak ditemukan
        for i in range(7):
            with open(File[i],'w',newline='') as savedfiles:
                csv_writer = csv.writer(savedfiles,delimiter=',')
                j = 0
                while (Filename[i][j] != None):
                    try:
                        csv_writer.writerow(Filename[i][j])
                        j += 1
                    except:
                        break
        print('Success!')


def upgrade(): # BONUS 
    username = input("Masukkan username yang ingin di-upgrade: ")
    arrUser = Filename[0]
    biaya = 200000
    i = 0
    while (arrUser[i] != None):
        if (arrUser[i][3] == username): # Mengecek apakah username terdaftar
            if (arrUser[i][5] != "Golden"):
                saldo = int(arrUser[i][6]) # Mengambil jumlah saldo dari 
                saldo -= biaya
                if (saldo < 0):
                    print("Saldo tidak mencukupi untuk upgrade! Silakan isi saldo terlebih dahulu")
                else: # saldo >= 0
                    arrUser[i][5] = "Golden"
                    arrUser[i][6] = saldo
                    print("Akun telah di-upgrade")
                break
            else: # Status akun telah "Golden"
                print("Akun ini telah di-upgrade sebelumnya.")
                break
        i += 1
    Filename[0] = arrUser
    return Filename


#BONUS BEST WAHANA
def best_wahana():
    arrWahana = Filename[1] # inisiasi array wahana
    arrBeli = Filename[2] # inisiasi array pembelian
    n = 0
    while (arrWahana[n] != None): # Menghitung banyak baris file wahana
        n += 1
    count = [[0 for j in range (3)] for i in range (n-1)] # Membuat array baru untuk total tiket per wahana
    for i in range (1,n):
        count[i-1] = [0,arrWahana[i][0],arrWahana[i][1]] # [0] = ID wahana ; [1] = nama wahana
        j = 0
        while (arrBeli[j] != None): # menghitung jumlah tiket wahana dari file pembelian tiket
            if (arrBeli[j][2] == arrWahana[i][0]):
                count[i-1][0] += int(arrBeli[j][3])
            j += 1
    
    for i1 in range(n-2): # mengurutkan array berdasarkan total penjualan tiket (besar ke kecil)
        for i2 in range(i1+1,n-1):
            if (count[i1][0] <= count[i2][0]):
                temp = count[i2]
                count[i2] = count[i1]
                count[i1] = temp
    for i in range (3): # menampilkan ranking wahana berdasarkan tiket
        print("{} | {} | {} | {}".format(i+1,count[i][1],count[i][2],count[i][0]))


def exit(): # Sebelum keluar, akan ditawarkan opsi untuk menyimpan
    print('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?',end=' ')
    choice = input()
    while not (choice == 'Y' or choice == 'y' or choice == 'N' or choice == 'n'): # Input divalidasi dahulu
        print('Input error!')
        print('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?', end=' ')
        choice = input()
    if choice == 'Y' or choice == 'y':
        save()
    index = False
    print("Anda telah keluar dari permainan. Sampai jumpa kembali!")
    return index
"""
---------------------------------------------------------------------------------------------------------
"""

session = True

print("Selamat Datang di Willy Wangky, 'Not Just A Chocolate Factory'")
print("Untuk memulai silakan masukkan (load) data-data terlebih dahulu")
print()
Filename = load()
a = input("\n(Tekan ENTER untuk lanjut)")
print()

while (session):
    clear()
    print("Willy Wangky, Dunia Bermain Impian Anda!")
    print("Silakan Login terlebih dahulu")
    print()
    admin,un,birth,height,role = login()
    index = True
    a = input("\n(Tekan ENTER untuk lanjut)")
    while (index):
        clear()
        if (admin):
            print("SELAMAT DATANG DI WILLY WANGKY!!!")
            print()
            print("Silakan pilih opsi di bawah ini:")
            print("1. Signup")
            print("2. Cari Pemain")
            print("3. Upgrade Akun")
            print("4. Lihat Kritik dan Saran")
            print("5. Tambah Wahana Baru")
            print("6. Top Up Saldo Pemain")
            print("7. Lihat Riwayat Wahana")
            print("8. Best Wahana")
            print("9. Lihat Jumlah Tiket Pemain")
            print("10. Save")
            print("11. Exit")
            print()
            pilih = int(input())
            clear()
            if (pilih == 1):
                print("$ Sign Up\n")
                signup()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 2):
                print("$ Cari Pemain\n")
                cari_pemain()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 3):
                print("$ Upgrade Akun\n")
                upgrade()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 4):
                print("$ Lihat Kritik Saran\n")
                lihat_laporan()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 5):
                print("$ Tambah Wahana\n")
                tambah_wahana()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 6):
                print("$ Top Up Saldo Pemain\n")
                topup()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 7):
                print("$ Lihat Riwayat Wahana\n")
                riwayat_wahana()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 8):
                print("$ Best Wahana\n")
                best_wahana()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 9):
                print("$ Lihat Jumlah Tiket Pemain\n")
                jumlah_tiket()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 10):
                print("$ Simpan Data\n")
                save()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 11):
                print("$ Exit\n")
                index = exit()
                a = input("\n(Tekan ENTER untuk lanjut)")
            else:
                print("Masukan tidak dikenal!")
                print("Silakan masukkan ulang opsi.")
                a = input("\n(Tekan ENTER untuk lanjut)")
        if (not admin):
            print("SELAMAT DATANG DI WILLY WANGKY!!!")
            print()
            print("Silakan pilih opsi di bawah ini:")
            print("1. Cari Wahana")
            print("2. Beli Tiket")
            print("3. Pakai Tiket")
            print("4. Refund")
            print("5. Kritik Saran")
            print("6. Save")
            print("7. Exit")
            print()
            pilih = int(input())
            clear()
            if (pilih == 1):
                print("$ Cari Wahana\n")
                cari_wahana()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 2):
                print("$ Beli Tiket\n")
                beli_tiket(un,birth,height,role)
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 3):
                print("$ Gunakan Tiket\n")
                pakai_tiket(un)
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 4):
                print("$ Refund Tiket\n")
                refund(un,role)
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 5):
                print("$ Tulis Kritik / Saran\n")
                kritik_saran(un)
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 6):
                print("$ Simpan Data\n")
                save()
                a = input("\n(Tekan ENTER untuk lanjut)")
            elif (pilih == 7):
                print("$ Exit\n")
                index = exit()
                a = input("\n(Tekan ENTER untuk lanjut)")
            else:
                print("Masukan tidak dikenal!")
                print("Silakan masukkan ulang opsi.")
                a = input("\n(Tekan ENTER untuk lanjut)")
                
