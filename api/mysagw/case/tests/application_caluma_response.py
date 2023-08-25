CALUMA_DATA_FULL = {
    "data": {
        "node": {
            "document": {
                "dossier_nr": {"edges": [{"node": {"value": "2022-0001"}}]},
                "verteilplan": {
                    "edges": [
                        {
                            "node": {
                                "stringValue": "verteilplan-nr-vp-2022",
                                "question": {
                                    "__typename": "ChoiceQuestion",
                                    "infoText": "",
                                    "label": "Verteilplan",
                                    "choiceOptions": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "slug": "verteilplan-nr-vp-2021",
                                                    "label": "2021",
                                                },
                                            },
                                            {
                                                "node": {
                                                    "slug": "verteilplan-nr-vp-2022",
                                                    "label": "2022",
                                                },
                                            },
                                            {
                                                "node": {
                                                    "slug": "verteilplan-nr-vp-2023",
                                                    "label": "2023",
                                                },
                                            },
                                        ],
                                    },
                                },
                            },
                        },
                    ],
                },
                "answers": {
                    "edges": [
                        {
                            "node": {
                                "question": {
                                    "slug": "test-many-multiple-choices",
                                    "meta": {},
                                },
                                "listValue": [
                                    "test-many-multiple-choices-choice-3",
                                    "test-many-multiple-choices-choice-6",
                                    "test-many-multiple-choices-choice-11",
                                ],
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-table", "meta": {}},
                                "tableValue": [
                                    {
                                        "answers": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-1"},
                                                        "stringValue": "Foo",
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-2"},
                                                        "integerValue": 2,
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-3"},
                                                        "floatValue": 2.2,
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-4"},
                                                        "stringValue": "row-4-choice-1",
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-5"},
                                                        "listValue": ["row-5-choice-3"],
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                    {
                                        "answers": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-1"},
                                                        "stringValue": "Bar",
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-2"},
                                                        "integerValue": 4,
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-3"},
                                                        "floatValue": 5.5,
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-4"},
                                                        "stringValue": "row-4-choice-2",
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "question": {"slug": "row-5"},
                                                        "listValue": [
                                                            "row-5-choice-3",
                                                            "row-5-choice-1",
                                                        ],
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                ],
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-date", "meta": {}},
                                "dateValue": "2022-10-14",
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-many-choices", "meta": {}},
                                "stringValue": "test-many-choices-choice-7",
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-textarea", "meta": {}},
                                "stringValue": "Bar\n\nBaz",
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-top-level", "meta": {}},
                                "stringValue": "some value",
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-text", "meta": {}},
                                "stringValue": "Foo",
                            },
                        },
                        {
                            "node": {
                                "question": {
                                    "slug": "test-multiple-choice",
                                    "meta": {},
                                },
                                "listValue": [
                                    "test-multiple-choice-choice-1",
                                    "test-multiple-choice-choice-3",
                                ],
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-calc", "meta": {}},
                                "floatValue": 46.5,
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-choice", "meta": {}},
                                "stringValue": "test-choice-choice-2",
                            },
                        },
                        {
                            "node": {
                                "question": {"slug": "test-file", "meta": {}},
                                "filesValue": [
                                    {
                                        "name": "small.png",
                                        "downloadUrl": "https://mysagw.local/caluma-media/download-url-small.png",
                                        "metadata": {
                                            "content_type": "image/png",
                                        },
                                    },
                                    {
                                        "name": "big.png",
                                        "downloadUrl": "https://mysagw.local/caluma-media/download-url-big.png",
                                        "metadata": {
                                            "content_type": "image/png",
                                        },
                                    },
                                    {
                                        "name": "long.png",
                                        "downloadUrl": "https://mysagw.local/caluma-media/download-url-long.png",
                                        "metadata": {
                                            "content_type": "image/png",
                                        },
                                    },
                                    {
                                        "name": "wide.png",
                                        "downloadUrl": "https://mysagw.local/caluma-media/download-url-wide.png",
                                        "metadata": {
                                            "content_type": "image/png",
                                        },
                                    },
                                ],
                            },
                        },
                        {
                            "node": {
                                "question": {
                                    "slug": "test-float",
                                    "meta": {"waehrung": "€"},
                                },
                                "floatValue": 23.5,
                            },
                        },
                        {
                            "node": {
                                "question": {
                                    "slug": "test-int",
                                    "meta": {"waehrung": "chf"},
                                },
                                "integerValue": 23,
                            },
                        },
                    ],
                },
                "form": {
                    "slug": "test-download",
                    "name": "Test Download",
                    "questions": {
                        "edges": [
                            {
                                "node": {
                                    "__typename": "FormQuestion",
                                    "slug": "test-form",
                                    "label": "Test form",
                                    "infoText": "",
                                    "subForm": {
                                        "slug": "test-download-types",
                                        "name": "Test Download Types",
                                        "questions": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "__typename": "StaticQuestion",
                                                        "slug": "test-static",
                                                        "label": "Test static",
                                                        "infoText": "",
                                                        "meta": {"waehrung": "chf"},
                                                        "staticContent": "Some static content",
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "TextQuestion",
                                                        "slug": "test-text",
                                                        "label": "Test text",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "TextareaQuestion",
                                                        "slug": "test-textarea",
                                                        "label": "Test textarea",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "IntegerQuestion",
                                                        "slug": "test-int",
                                                        "label": "Test int",
                                                        "infoText": "",
                                                        "meta": {"waehrung": "chf"},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "FloatQuestion",
                                                        "slug": "test-float",
                                                        "label": "Test float",
                                                        "infoText": "",
                                                        "meta": {"waehrung": "€"},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "MultipleChoiceQuestion",
                                                        "slug": "test-multiple-choice",
                                                        "label": "Test multiple choice",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "multipleChoiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "ChoiceQuestion",
                                                        "slug": "test-choice",
                                                        "label": "Test choice",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "choiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "FilesQuestion",
                                                        "slug": "test-file",
                                                        "label": "Test file",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "DateQuestion",
                                                        "slug": "test-date",
                                                        "label": "Test date",
                                                        "infoText": "Bitte geben Sie das Datum ein.",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "CalculatedFloatQuestion",
                                                        "slug": "test-calc",
                                                        "label": "Test calc",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "TableQuestion",
                                                        "slug": "test-table",
                                                        "label": "Test table",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "rowForm": {
                                                            "slug": "test-table-form",
                                                            "name": "Test table form",
                                                            "questions": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "__typename": "TextQuestion",
                                                                            "slug": "row-1",
                                                                            "label": "Row 1",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "IntegerQuestion",
                                                                            "slug": "row-2",
                                                                            "label": "Row 2",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "FloatQuestion",
                                                                            "slug": "row-3",
                                                                            "label": "Row 3",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "ChoiceQuestion",
                                                                            "slug": "row-4",
                                                                            "label": "Row 4",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                            "choiceOptions": {
                                                                                "edges": [
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-1",
                                                                                            "label": "choice 1",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-2",
                                                                                            "label": "choice 2",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-3",
                                                                                            "label": "choice 3",
                                                                                        },
                                                                                    },
                                                                                ],
                                                                            },
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "MultipleChoiceQuestion",
                                                                            "slug": "row-5",
                                                                            "label": "Row 5",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                            "multipleChoiceOptions": {
                                                                                "edges": [
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-1",
                                                                                            "label": "choice 1",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-2",
                                                                                            "label": "choice 2",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-3",
                                                                                            "label": "choice 3",
                                                                                        },
                                                                                    },
                                                                                ],
                                                                            },
                                                                        },
                                                                    },
                                                                ],
                                                            },
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "ChoiceQuestion",
                                                        "slug": "test-many-choices",
                                                        "label": "Test Many Choices",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "choiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-4",
                                                                        "label": "choice 4",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-5",
                                                                        "label": "choice 5",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-6",
                                                                        "label": "choice 6",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-7",
                                                                        "label": "choice 7",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-8",
                                                                        "label": "choice 8",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-9",
                                                                        "label": "choice 9",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-10",
                                                                        "label": "choice 10",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-11",
                                                                        "label": "choice 11",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "StaticQuestion",
                                                        "slug": "submit-button",
                                                        "label": "Submit button",
                                                        "infoText": "",
                                                        "staticContent": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "MultipleChoiceQuestion",
                                                        "slug": "test-many-multiple-choices",
                                                        "label": "Test Many Multiple Choices",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "multipleChoiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-4",
                                                                        "label": "choice 4",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-5",
                                                                        "label": "choice 5",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-6",
                                                                        "label": "choice 6",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-7",
                                                                        "label": "choice 7",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-8",
                                                                        "label": "choice 8",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-9",
                                                                        "label": "choice 9",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-10",
                                                                        "label": "choice 10",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-11",
                                                                        "label": "choice 11",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "node": {
                                    "__typename": "TextQuestion",
                                    "slug": "test-top-level",
                                    "label": "Test top level",
                                    "infoText": "<p>Eine Info.</p>",
                                    "meta": {},
                                },
                            },
                        ],
                    },
                },
            },
        },
    },
}


CALUMA_DATA_EMPTY = {
    "data": {
        "node": {
            "document": {
                "dossier_nr": {"edges": [{"node": {"value": "2022-0001"}}]},
                "verteilplan": {"edges": []},
                "answers": {"edges": []},
                "form": {
                    "slug": "test-download",
                    "name": "Test Download",
                    "questions": {
                        "edges": [
                            {
                                "node": {
                                    "__typename": "FormQuestion",
                                    "slug": "test-form",
                                    "label": "Test form",
                                    "infoText": "",
                                    "meta": {},
                                    "subForm": {
                                        "slug": "test-download-types",
                                        "name": "Test Download Types",
                                        "questions": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "__typename": "TextQuestion",
                                                        "slug": "test-text",
                                                        "label": "Test text",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "TextareaQuestion",
                                                        "slug": "test-textarea",
                                                        "label": "Test textarea",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "IntegerQuestion",
                                                        "slug": "test-int",
                                                        "label": "Test int",
                                                        "infoText": "",
                                                        "meta": {"waehrung": "chf"},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "FloatQuestion",
                                                        "slug": "test-float",
                                                        "label": "Test float",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "MultipleChoiceQuestion",
                                                        "slug": "test-multiple-choice",
                                                        "label": "Test multiple choice",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "multipleChoiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-multiple-choice-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "ChoiceQuestion",
                                                        "slug": "test-choice",
                                                        "label": "Test choice",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "choiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-choice-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "FilesQuestion",
                                                        "slug": "test-file",
                                                        "label": "Test file",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "StaticQuestion",
                                                        "slug": "test-static",
                                                        "label": "Test static",
                                                        "infoText": "",
                                                        "staticContent": "Some static content",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "DateQuestion",
                                                        "slug": "test-date",
                                                        "label": "Test date",
                                                        "infoText": "Bitte geben Sie das Datum ein.",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "CalculatedFloatQuestion",
                                                        "slug": "test-calc",
                                                        "label": "Test calc",
                                                        "infoText": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "TableQuestion",
                                                        "slug": "test-table",
                                                        "label": "Test table",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "rowForm": {
                                                            "slug": "test-table-form",
                                                            "name": "Test table form",
                                                            "questions": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "__typename": "TextQuestion",
                                                                            "slug": "row-1",
                                                                            "label": "Row 1",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "IntegerQuestion",
                                                                            "slug": "row-2",
                                                                            "label": "Row 2",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "FloatQuestion",
                                                                            "slug": "row-3",
                                                                            "label": "Row 3",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "ChoiceQuestion",
                                                                            "slug": "row-4",
                                                                            "label": "Row 4",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                            "choiceOptions": {
                                                                                "edges": [
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-1",
                                                                                            "label": "choice 1",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-2",
                                                                                            "label": "choice 2",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-4-choice-3",
                                                                                            "label": "choice 3",
                                                                                        },
                                                                                    },
                                                                                ],
                                                                            },
                                                                        },
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "__typename": "MultipleChoiceQuestion",
                                                                            "slug": "row-5",
                                                                            "label": "Row 5",
                                                                            "infoText": "",
                                                                            "meta": {},
                                                                            "multipleChoiceOptions": {
                                                                                "edges": [
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-1",
                                                                                            "label": "choice 1",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-2",
                                                                                            "label": "choice 2",
                                                                                        },
                                                                                    },
                                                                                    {
                                                                                        "node": {
                                                                                            "slug": "row-5-choice-3",
                                                                                            "label": "choice 3",
                                                                                        },
                                                                                    },
                                                                                ],
                                                                            },
                                                                        },
                                                                    },
                                                                ],
                                                            },
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "ChoiceQuestion",
                                                        "slug": "test-many-choices",
                                                        "label": "Test Many Choices",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "choiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-4",
                                                                        "label": "choice 4",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-5",
                                                                        "label": "choice 5",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-6",
                                                                        "label": "choice 6",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-7",
                                                                        "label": "choice 7",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-8",
                                                                        "label": "choice 8",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-9",
                                                                        "label": "choice 9",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-10",
                                                                        "label": "choice 10",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-choices-choice-11",
                                                                        "label": "choice 11",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "StaticQuestion",
                                                        "slug": "submit-button",
                                                        "label": "Submit button",
                                                        "infoText": "",
                                                        "staticContent": "",
                                                        "meta": {},
                                                    },
                                                },
                                                {
                                                    "node": {
                                                        "__typename": "MultipleChoiceQuestion",
                                                        "slug": "test-many-multiple-choices",
                                                        "label": "Test Many Multiple Choices",
                                                        "infoText": "",
                                                        "meta": {},
                                                        "multipleChoiceOptions": {
                                                            "edges": [
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-1",
                                                                        "label": "choice 1",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-2",
                                                                        "label": "choice 2",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-3",
                                                                        "label": "choice 3",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-4",
                                                                        "label": "choice 4",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-5",
                                                                        "label": "choice 5",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-6",
                                                                        "label": "choice 6",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-7",
                                                                        "label": "choice 7",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-8",
                                                                        "label": "choice 8",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-9",
                                                                        "label": "choice 9",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-10",
                                                                        "label": "choice 10",
                                                                    },
                                                                },
                                                                {
                                                                    "node": {
                                                                        "slug": "test-many-multiple-choices-choice-11",
                                                                        "label": "choice 11",
                                                                    },
                                                                },
                                                            ],
                                                        },
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "node": {
                                    "__typename": "TextQuestion",
                                    "slug": "test-top-level",
                                    "label": "Test top level",
                                    "infoText": "<p>Eine Info.</p>",
                                    "meta": {},
                                },
                            },
                        ],
                    },
                },
            },
        },
    },
}
