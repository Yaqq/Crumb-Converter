import json

if __name__ == "__main__":
    lang = ["en", "es", "fr", "pt"]

    clothingTypes = ["COLOUR", "HEAD", "FACE", "NECK", "BODY",
                     "HAND", "FEET", "FLAG", "PHOTO", "OTHER"]

    paperdollDepth = {
        "7500": "PAPERDOLLDEPTH_TOP_LAYER",
        "7000": "PAPERDOLLDEPTH_HAND_LAYER",
        "6500": "PAPERDOLLDEPTH_BETWEEN_HAND_AND_HEAD",
        "6000": "PAPERDOLLDEPTH_HEAD_LAYER",
        "5500": "PAPERDOLLDEPTH_BETWEEN_HEAD_AND_FACE",
        "5000": "PAPERDOLLDEPTH_FACE_LAYER",
        "4500": "PAPERDOLLDEPTH_BETWEEN_FACE_AND_NECK",
        "3500": "PAPERDOLLDEPTH_BETWEEN_NECK_AND_BODY",
        "3000": "PAPERDOLLDEPTH_BODY_LAYER",
        "2500": "PAPERDOLLDEPTH_BETWEEN_BODY_AND_FEET",
        "2000": "PAPERDOLLDEPTH_FEET_LAYER",
        "1500": "PAPERDOLLDEPTH_BETWEEN_FEET_AND_BACK",
        "1000": "PAPERDOLLDEPTH_BACK_LAYER",
        "500": "PAPERDOLLDEPTH_BOTTOM_LAYER",
    }

    exclusives = [
        "INVENTORY_EXCLUSIVE",
        "INVENTORY_SUPER_EXCLUSIVE",
        "INVENTORY_SUPER_EXCLUSIVE"
    ]

    jsonFile = open("crumbs/en/paper_items.json", "r")
    itemsJson = json.load(jsonFile)
    jsonFile.close()

    open("dump/paper_items.d", "w").close()
    convertFile = open("dump/paper_items.d", "w")

    for item in itemsJson:
        itemId = item["paper_item_id"]
        itemType = clothingTypes[item["type"] - 1]
        isMember = "true" if item["is_member"] else "false"
        itemCost = item["cost"]

        itemData = "type:%s,cost:%d,is_member:%s" % (itemType, itemCost, isMember)

        tourGuide = ",make_tour_guide:true" if "make_tour_guide" in item else ""
        isBack = ",is_back:true" if "is_back" in item else ""
        noPurchasePopup = ",noPurchasePopup:true" if "noPurchasePopup" in item else ""
        customDepth = ",customDepth:shell.%s" % (paperdollDepth[item["customDepth"]]) if "customDepth" in item else ""
        makeSecretAgent = ",make_secret_agent:true" if "make_secret_agent" in item else ""
        isMedal = ",is_medal:true" if "is_medal" in item else ""
        isGift = ",is_gift:true" if "is_gift" in item else ""
        exclusive = ",exclusive:shell.%s" % (exclusives[int(item["exclusive"]) - 1]) if "exclusive" in item else ""

        itemData += "%s%s%s%s%s%s%s%s" % (tourGuide, isBack, noPurchasePopup, customDepth, makeSecretAgent,
                                          isMedal, isGift, exclusive)

        convertFile.write("paper_crumbs[%s] = {%s};\n" % (itemId, itemData))

    convertFile.write("\n\n");

    for language in lang:
        jsonFile = open("crumbs/%s/paper_items.json" % language, "r")
        itemsJson = json.load(jsonFile)
        jsonFile.close()
        for item in itemsJson:
            itemId = item["paper_item_id"]
            itemName = json.dumps(item["label"])
            convertFile.write("paper_crumbs[%s] = {name:%s};\n" % (itemId, itemName))
    convertFile.close()

    jsonFile = open("crumbs/en/furniture_items.json", "r")
    furnitureJson = json.load(jsonFile)
    jsonFile.close()

    open("dump/furniture_items.d", "w").close()
    convertFile = open("dump/furniture_items.d", "w")

    furnitureTypes = [
        "TYPE_ROOM", "TYPE_WALL", "TYPE_FLOOR", "TYPE_WALL"
    ]

    furnitureSorts = [
        "SORT_ROOM", "SORT_WALL", "SORT_FLOOR", "SORT_PET"
    ]

    interactives = [
        "INTERACTIVE_PLAY", "INTERACTIVE_REST", "INTERACTIVE_FEED"
    ]

    for furniture in furnitureJson:
        furnitureId = furniture["furniture_item_id"]
        furnitureType = furnitureTypes[furniture["type"] - 1]
        furnitureSort = furnitureSorts[furniture["sort"] - 1]
        furnitureCost = furniture["cost"]

        furnitureData = "type:%s,sort:%s,cost:%d" % (furnitureType, furnitureSort, furnitureCost)

        interactive = ",interactive:%s" % (interactives[int(furniture["interactive"]) - 1]) if "interactive" in furniture else ""
        furnitureData += interactive

        convertFile.write("furniture_crumbs[%d] = {%s};\n" % (furnitureId, furnitureData))

    convertFile.write("\n\n")

    for language in lang:
        jsonFile = open("crumbs/%s/furniture_items.json" % language, "r")
        furnitureJson = json.load(jsonFile)
        jsonFile.close()
        for furniture in furnitureJson:
            furnitureId = furniture["furniture_item_id"]
            furnitureName = json.dumps(furniture["label"])

            convertFile.write("furniture_crumbs[%d] = {name:%s};\n" % (furnitureId, furnitureName))
    convertFile.close()

    jsonFile = open("crumbs/en/igloos.json", "r")
    igloosJson = json.load(jsonFile).values()
    jsonFile.close()

    open("dump/igloos.d", "w").close()
    convertFile = open("dump/igloos.d", "w")

    for igloo in igloosJson:
        iglooId = igloo["igloo_id"]
        iglooCost = igloo["cost"]

        convertFile.write("igloo_crumbs[%s] = {cost:%s};\n" % (iglooId, iglooCost))

    convertFile.write("\n\n")

    for language in lang:
        jsonFile = open("crumbs/%s/igloos.json" % language, "r")
        igloosJson = json.load(jsonFile).values()
        jsonFile.close()
        for igloo in igloosJson:
            iglooId = igloo["igloo_id"]
            iglooName = json.dumps(igloo["name"])

            convertFile.write("igloo_crumbs[%s] = {name:%s};\n" % (iglooId, iglooName))

    jsonFile = open("crumbs/en/igloo_floors.json", "r")
    floorsJson = json.load(jsonFile)
    jsonFile.close()

    open("dump/igloo_floors.d", "w").close()
    convertFile = open("dump/igloo_floors.d", "w")

    for floor in floorsJson:
        floorId = floor["igloo_floor_id"]
        floorCost = floor["cost"]

        convertFile.write("floor_crumbs[%s] = {cost:%s};\n" % (floorId, floorCost))

    convertFile.write("\n\n")

    for language in lang:
        jsonFile = open("crumbs/%s/igloo_floors.json" % language, "r")
        floorsJson = json.load(jsonFile)
        jsonFile.close()
        for floor in floorsJson:
            floorId = floor["igloo_floor_id"]
            floorName = json.dumps(floor["label"])

            convertFile.write("floor_crumbs[%s] = {name:%s};\n" % (floorId, floorName))
