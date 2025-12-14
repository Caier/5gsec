## 5G experiments

### Stuff

There is a [Modify Authentication Data](https://dstest.info/RestDict/Dictionary/8606.html) SBI endpoint in the `nudr-dr` service that allows to modify auth data of subscribers stored in the repository.

According to 3GPP TS 29.505: `Updates shall be limited to the sequenceNumber property. Attempts to patch any other attribute shall be rejected.`.

Open5GS follows this and their UDR implementation only supports modifying the SQN.
Free5GC's UDR though let's the requesting NF update every auth data, including the associated SUPI keys. Example request:

```bash
curl "http://<UDR_SOCKET>/nudr-dr/v2/subscription-data/<UE_ID>/authentication-data/authentication-subscription" \
    -X PATCH \
    --json '[{"op": "replace", "path": "/encOpcKey", "value": "666"}]'
```