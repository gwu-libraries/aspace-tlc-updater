class TopContainer:
    def __init__(self, top_container_json: dict):
        self.lock_version = top_container_json['lock_version']
        if 'barcode' in top_container_json:
            self.barcode = top_container_json['barcode']
        else:
            self.barcode = None
        self.indicator = top_container_json['indicator']
        self.type = top_container_json['type']
        self.created_by = top_container_json['created_by']
        self.last_modified_by = top_container_json['last_modified_by']
        self.create_time = top_container_json['create_time']
        self.system_mtime = top_container_json['system_mtime']
        self.user_mtime = top_container_json['user_mtime']
        self.jsonmodel_type = top_container_json['jsonmodel_type']
        self.display_string = top_container_json['display_string']
        self.long_display_string = top_container_json['long_display_string']
        self.container_locations = top_container_json['container_locations']
        self.active_restrictions = top_container_json['active_restrictions']
        self.series = top_container_json['series']
        self.collection = top_container_json['collection']
        self.restricted = top_container_json['restricted']
        self.is_linked_to_published_record = top_container_json['is_linked_to_published_record']

    def serialize(self, new_barcode):
        serialized_json = {
            "lock_version": self.lock_version,
            "barcode": new_barcode,
            "type": self.type,
            "indicator": self.indicator,
            "jsonmodel_type": self.jsonmodel_type,
            "container_locations": self.container_locations,
            "active_restrictions": self.active_restrictions,
            "series": self.series,
            "collection": self.collection,
            "restricted": self.restricted,
            "is_linked_to_published_record": self.is_linked_to_published_record
        }
        return serialized_json