#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:42:17 2020

@author: tommasodimario
"""


def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]
    permutation_list = []
    for i, el in enumerate(my_list):
        for permutation in permutations(my_list[:i]+my_list[i+1:]):
            permutation_list.append([el]+permutation)
    return permutation_list

def tu(s):
    xl = ''.maketrans('abcdefghijklmnopqrtuvwxyznžƀƚǆщӷҫзҝŧаɖξѡçӗšјӽӳϭlŏѻyıȁĉȱїцhъԁчҩʊσvҳэǉħdӓӡӝìǩвȥʌоԝєɀԛƒŀȏpŋmáӭǘaӄтίǚѥȃђҗϻȕόĳƭөώԇѫǹηīñơϼδԉсǡȫғφψӵςəÿɍƹϥмюrǐфŷҿƕöνѵåǳҧͱȼǰќοѳíӛкƺѩӈӂιӆԣΐљӎƪȑԏɉλхªңйƅǒĩԅqѕʒͻҏϣӹγϸѹрӟыɲχџԙúжіӣκűwoӧǜgďïɨԡҍßȯӻшȳȷӏjнӊăċѷԃӿǣьëȇϯқǔгεѭҵԍϡӥȩƽӌƥӑǎǯѿùxêԋӫœȸûүäёѯτɔуȍæȉƈͳǧύϝҡәԥƛҟǖĺøkеͽtͼυȹάɏƴǌeρésлҥѓȋҷuдϙȡήΰѝȧǵǫѧѣŕωҁɋѽͷҕяcћўҽϫȣiòǥԧԕҹϊþѐƾȴȿȵұƿčиǟõϳƫӱȓǽζȶżαϟβϩӕbҙǭɂέîüԗбҭӯŝàѱθzŉϋμƙóƣýҋπºґƌԟњпůƞðfƃһȅʀƍϧ', '                                                                                                                                                                                                                                                                                                                                                                                                             ')
    xu = ''.maketrans('ABCDEFGHIJKLMNOPQRTUVWXYZTȲȀѢΌYӍĂĴКȞǢȆΔȺÓԘԤJŇӪЧȦŠОȐѶϜİҚЛÙԄΗЉΆЙƬƲΝԎǂѮǱБÃШϮΧȢЀǊЗǼΡǬϪƓϘɄΈѼЏÎӚƇǏПĜҜԔǶԖƼԚƑДΜȨΟÁҔӐĎƳѠȻȮϢȒФЋƟȽГɈѦРϾÖÏǁǙΘÅΓŹИϨАҘЬЦЇӲӀҎËΊѸТѪȪŸƜҮԂǑȄҼΏÚCȌЊϦϽƊΛͰҞԜӞЕȖɊҦƤҤЪӠΞƁҢΎØѴӃÑΨƐȂӺΉІȎӼȔҰɃȊBҪԦŤУÇӖЩӁЯǓȠQEѺǷԆϤÞŢƖҀҾϏǨGӉŽЫÌҠͲȜÂԈÄϬӋÔǦВÉǾҌUҲǠҨSƮČӜӰҐМЍӔŮӬΣÜΠǤҴӒǪȾÊЖѤЄӤÐӸƔЮѬϠҺΑFŒҸǴÒXIϿDAŶǇΖǺƎЂǛѾMҒӇRȤӅҬZӴWХӢÕǮHΦƢЁVϺЃԀԢӶӘԊӮΫOϷĹҊԌƧLΪǞЭĈǸЌÛͶNѨԞѲҶɌϞСƸƘΥɎÍȈΚΤΒҖÆΕĢPНЎѰӦɁΩϚӾƻΙӨЈÀŦƄK', '                                                                                                                                                                                                                                                                                                                                                                                       ')
    s1 = s.translate(xl)
    s2 = s.translate(xu)
    return [s2[0],s1[0],s2[1],s1[1]]