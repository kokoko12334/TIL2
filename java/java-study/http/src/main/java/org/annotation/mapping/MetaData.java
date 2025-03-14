package org.annotation.mapping;

@AnnoMeta
public class MetaData {
    private String id;

    @AnnoMeta
    public void cal() {

    }

    public static void main(String[] args) {
        AnnoMeta annotation = MetaData.class.getAnnotation(AnnoMeta.class);
        System.out.println(annotation);
    }
}
