from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangoaccountstorage' # Must be replaced by your <storage_account_name>
    account_key = 'AKgCUPoxV+E7rWfJblUyH49iZ0kvF6BoD8pv1D52zUGDeLrbEXuBdGsdD98gWmIPe1X3ZCkNW1Ijy9kT31f4PQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangoaccountstorage' # Must be replaced by your storage_account_name
    account_key = 'KAOgKN5gVHDNpYINk91xh5H5nshAVLRrRv99tmD36hHKxsjy/6BPXMIkxFSDLVru06VoAnIgcIBJt99zqZaFuQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
	