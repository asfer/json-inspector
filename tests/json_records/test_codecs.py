from schematizer.json_records import codecs


def test_encode_decode_json():
    input_object = {'foo': 'bar'}
    encoded = codecs.encode_json(input_object)
    output_object = codecs.decode_json(encoded)
    assert output_object == input_object
