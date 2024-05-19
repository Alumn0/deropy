class WalletSimulator:
    active_wallet = None
    wallets = {}
    wallet_count = 0

    @staticmethod
    def reset():
        WalletSimulator.active_wallet = None
        WalletSimulator.wallets = {}
        WalletSimulator.wallet_count = 0

    @staticmethod
    def find_wallet_id_from_string(string_address):
        for idx, wallet in WalletSimulator.wallets.items():
            if wallet.string_address == string_address:
                return idx
        raise Exception("Wallet not found")

    @staticmethod
    def find_wallet_id_from_raw(raw_address):
        for idx, wallet in WalletSimulator.wallets.items():
            if wallet.raw_address == raw_address:
                return idx
        raise Exception("Wallet not found")

    @staticmethod
    def get_wallet_from_raw(raw_address):
        idx = WalletSimulator.find_wallet_id_from_raw(raw_address)
        return WalletSimulator.get_wallet_from_id(idx)

    @staticmethod
    def get_wallet_from_id(idx):
        return WalletSimulator.wallets[idx]

    @staticmethod
    def get_raw_address():
        return WalletSimulator.wallets[WalletSimulator.active_wallet].raw_address

    @staticmethod
    def get_string_address():
        return WalletSimulator.wallets[WalletSimulator.active_wallet].string_address

    @staticmethod
    def get_raw_address_from_id(idx):
        return WalletSimulator.wallets[idx].raw_address

    def get_string_address_from_id(idx):
        return WalletSimulator.wallets[idx].string_address

    @staticmethod
    def is_initialized():
        return WalletSimulator.active_wallet is not None
