/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ibd.table;

import static ibd.table.RecordManager.BLOCKS_WRITE;
import static ibd.table.RecordManager.BLOCKS_READ;

import java.io.File;
import java.io.IOException;
import java.util.List;

/**
 *
 * @author ferna
 */
public class Main {
    public static void main(String[] args) throws IOException {
        for (int firstListSize = 0; firstListSize <= 1000; firstListSize += 250) {
            int secondListSize = 1000 - firstListSize;

                for (double splitFactor = 0; splitFactor <= 1; splitFactor += 0.1) {


                String fileName = "./records.dat";
                Table table = new Table(fileName, RecordManager.STRING_TYPE);

                table.createTable(256, 32, splitFactor);

                table.openTable();

                IDGenerator gen = new IDGenerator();
                gen.generate(0, 10000, firstListSize, secondListSize);
                BLOCKS_WRITE = 0;
                List<Integer> ids = gen.getSortedList();
                int lastId = -1;
                for (int i = 0; i < ids.size(); i++) {
                    int id = ids.get(i);
                    // System.out.println("adding " + id);
                    table.insertRecord(new StringRecord(id, "rec:" + id));
                    lastId = id;
                }

                ids = gen.getShuffledList();
                for (int i = 0; i < ids.size(); i++) {
                    int id = ids.get(i);
                    // System.out.println("adding " + id);
                    table.insertRecord(new StringRecord(id, "rec:" + id));
                    lastId = id;
                }

                System.out.println(splitFactor + " " + firstListSize + " " + secondListSize + " " + BLOCKS_WRITE + " " + table.manager.getBlocksCount());

                table.closeTable();
            }
        }

        
        
//        table.openTable();
//        List<Record> records = table.readAllRecords();
//        int x = 0;
//        for (Record record : records) {
//            System.out.println(x + "-" + record.getContent());
//             x++;
//        }
        
//        BLOCKS_READ = 0;
//        System.out.println("searching for "+lastId);
//        Record rec = table.readRecord(lastId);
//        if (rec!=null){
//            System.out.println(rec.getContent());
//        }
//        
//        System.out.println("blocks read to perform the search: " + BLOCKS_READ);

    }
}
