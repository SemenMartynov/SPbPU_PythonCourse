import doctest

# TODO Написать 3 класса с документацией и аннотацией типов


class CryptoCurrency:
    """
    Класс описывающий криптовалюту.
    """

    def __init__(self, symbol: str, blockchain: str, supply: float):
        """
        Инициализация криптовалюты.

        :param symbol: Символ криптовалюты
        :param blockchain: Название блокчейна
        :param supply: Общее количество монет в обороте

        :type symbol: str
        :type blockchain: str
        :type supply: float

        >>> btc = CryptoCurrency('BTC', 'Bitcoin', 100500.0)
        """
        if not symbol or not isinstance(symbol, str):
            raise ValueError("Symbol должен быть непустой строкой")
        if not blockchain or not isinstance(blockchain, str):
            raise ValueError("Blockchain должен быть непустой строкой")
        if not isinstance(supply, float) or supply <= 0:
            raise ValueError("Supply должен быть положительным числом")

        self.symbol = symbol
        self.blockchain = blockchain
        self.supply = supply

    def send(self, address: str, amount: float):
        """
        Отправка заданного количества криптовалюты на указанный адрес.

        :param address: Адрес получателя
        :param amount: Количество криптовалюты

        :type address: str
        :type amount: float

        >>> btc = CryptoCurrency('BTC', 'Bitcoin', 100500.0)
        >>> btc.send('1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 0.5)
        """
        pass

    def check_balance(self) -> float:
        """
        Проверка баланса криптовалюты.

        >>> btc = CryptoCurrency('BTC', 'Bitcoin', 100500.0)
        >>> btc.check_balance()
        """
        pass


class CryptoToken:
    """
    Класс описывающий криптотокен.
    """

    def __init__(self, name: str, supply: int, owner: str):
        """
        Инициализация криптотокена.

        :param name: Название токена
        :param supply: Общее количество токенов
        :param owner: Владелец токена

        :type name: str
        :type supply: int
        :type owner: str

        >>> usdt = CryptoToken('TetherUSD', 1000000000, 'Tether Limited')
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name должен быть непустой строкой")
        if not isinstance(supply, int) or supply <= 0:
            raise ValueError("Supply должен быть положительным целым числом")
        if not owner or not isinstance(owner, str):
            raise ValueError("Owner должен быть непустой строкой")

        self.name = name
        self.supply = supply
        self.owner = owner

    def mint(self, amount: int):
        """
        Эмиссия новых токенов.

        :param amount: Количество токенов для эмиссии

        :type amount: int

        >>> usdt = CryptoToken('TetherUSD', 1000000000, 'Tether Limited')
        >>> usdt.mint(1000000)
        """
        pass

    def burn(self, amount: int):
        """
        Уничтожение (сжигание) токенов.

        :param amount: Количество токенов для уничтожения

        :type amount: int

        >>> usdt = CryptoToken('TetherUSD', 1000000000, 'Tether Limited')
        >>> usdt.burn(10000)
        """
        pass


class NonFungibleToken:
    """
    Класс, описывающий невзаимозаменяемый токен (NFT).
    """

    def __init__(self, name: str, token_id: int, creator: str):
        """
        Инициализация невзаимозаменяемого токена.

        :param name: Название NFT
        :param token_id: Уникальный идентификатор токена
        :param creator: Автор NFT

        :type name: str
        :type token_id: int
        :type creator: str

        >>> art = NonFungibleToken('CryptoPunk#3100', 3310, 'Larva Labs')
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name должен быть непустой строкой")
        if not isinstance(token_id, int) or token_id <= 0:
            raise ValueError("Token ID должен быть положительным целым числом")
        if not creator or not isinstance(creator, str):
            raise ValueError("Creator должен быть непустой строкой")

        self.name = name
        self.token_id = token_id
        self.creator = creator

    def transfer(self, to_owner: str):
        """
        Передача владения NFT другому пользователю.

        :param to_owner: Новый владелец NFT

        :type to_owner: str

        >>> art = NonFungibleToken('CryptoPunk#3100', 3310, 'Larva Labs')
        >>> art.transfer('0x0...newowner')
        """
        pass

    def display_info(self):
        """
        Отображение информации об NFT.

        >>> art = NonFungibleToken('CryptoPunk#3100', 3310, 'Larva Labs')
        >>> art.display_info()
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
