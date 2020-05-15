#GRAMMAR_ROOT S

Lang -> 'англ' | 'русс' | 'рус';
Date->AnyWord<kwtype = "даты">;
Brackets->LBracket (AnyWord*) Lang (Comma) (Hyphen) AnyWord* interp(Albums.Translate) RBracket;
FirstPart->AnyWord* interp(Albums.Name) (Brackets) Hyphen Adj;
FullName->AnyWord<h-reg1>* AnyWord<h-reg1>;
Auth -> AnyWord * 'альбом'  AnyWord<l-reg>* FullName interp(Albums.Author) Comma;
S->FirstPart Auth  AnyWord*  Date interp(Albums.Date) (AnyWord *)(Comma);
