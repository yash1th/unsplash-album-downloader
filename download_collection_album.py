from download_user_album import *

COLLECTION_URL = 'https://api.unsplash.com/collections/'


def get_collections(cid, mode, curated_flag=False):
    title = '-unsplash-'
    if curated_flag:
        collection, s = get_response(COLLECTION_URL + 'curated/' + cid, {'client_id': ACCESS_KEY})
        title = '-curated' + title
    else:
        collection, s = get_response(COLLECTION_URL + cid, {'client_id': ACCESS_KEY})
        title = title + 'collection-'
    photo_ids = get_photo_ids(collection['links']['photos'], collection['total_photos'], mode)
    user_directory = os.getcwd() + r'/' + collection['user']['name'] + title + collection['title'].replace('/',
                                                                                                           '_') + '-' + mode  # replaces / with underscore
    save_photos(user_directory, photo_ids)


def collection_main():
    args = collection_parse_args()
    get_collections(args.collection_id, args.size, args.curated)


def collection_parse_args():
    parser = argparse.ArgumentParser(description='arguments of how to download collections')
    parser.add_argument('collection_id', type=str.lower, help='id of the collection that needs to be downloaded')
    parser.add_argument('-c', '--curated', action='store_true', help='provide if its a curated collection')
    parser.add_argument('size', type=str.lower, nargs='?', default='regular',
                        choices=['raw', 'full', 'regular', 'small', 'thumb'])
    return parser.parse_args()


if __name__ == '__main__':
    collection_main()
