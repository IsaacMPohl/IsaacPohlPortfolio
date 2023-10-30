package com.example.madlib;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText adj1TXTBox = findViewById(R.id.adj1TXTBox);
        EditText adj2TXTBox = findViewById(R.id.adj2TXTBox);
        EditText adj3TXTBox = findViewById(R.id.adj3TXTBox);
        EditText noun4TXTBox = findViewById(R.id.noun4TXTBox);
        EditText adj5TXTBox = findViewById(R.id.adj5TXTBox);
        EditText adj6TXTBox = findViewById(R.id.adj6TXTBox);
        EditText adj7TXTBox = findViewById(R.id.adj7TXTBox);
        EditText noun8TXTBox = findViewById(R.id.noun8TXTBox);
        LinearLayout mainVerticalLayout = findViewById(R.id.mainVerticalLayout);
        LinearLayout outPutLinear = findViewById(R.id.outPutLinear);
        ImageView pic = findViewById(R.id.imageView4);

        Button madLib1BTN = findViewById(R.id.madLib1BTN);
        Button madLib2BTN = findViewById(R.id.madLib2BTN);
        Button madLib3BTN = findViewById(R.id.madLib3BTN);
        Button randomBTN = findViewById(R.id.randomBTN);
        Button appearBTN = findViewById(R.id.appearBTN);
        outPutLinear.setVisibility(View.GONE);



        TextView outPutTXT = findViewById(R.id.outPutTXT);

        madLib1BTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String adj1TXT = String.valueOf(adj1TXTBox.getText());
                String adj2TXT = String.valueOf(adj2TXTBox.getText());
                String adj3TXT = String.valueOf(adj3TXTBox.getText());
                String noun4TXT = String.valueOf(noun4TXTBox.getText());
                String adj5TXT = String.valueOf(adj5TXTBox.getText());
                String adj6TXT = String.valueOf(adj6TXTBox.getText());
                String adj7TXT = String.valueOf(adj7TXTBox.getText());
                String noun8TXT = String.valueOf(noun8TXTBox.getText());

                outPutTXT.setText("Deep within the " + adj1TXT + " forest, I stumbled upon a " + adj2TXT + " clearing. In the center, there was a " + adj3TXT + " " + noun4TXT + " surrounded by " + adj5TXT + " trees. As I approached, I noticed a " + adj6TXT + " glow emanating from the " + adj7TXT + " leaves. I reached out and touched them, and suddenly, I felt a surge of " + noun8TXT + ".");
                outPutLinear.setVisibility(View.VISIBLE);
                mainVerticalLayout.setVisibility(View.GONE);
                pic.setImageDrawable(getDrawable(R.drawable.forest));



            }
        });
        madLib2BTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String adj1TXT = String.valueOf(adj1TXTBox.getText());
                String adj2TXT = String.valueOf(adj2TXTBox.getText());
                String adj3TXT = String.valueOf(adj3TXTBox.getText());
                String noun4TXT = String.valueOf(noun4TXTBox.getText());
                String adj5TXT = String.valueOf(adj5TXTBox.getText());
                String adj6TXT = String.valueOf(adj6TXTBox.getText());
                String adj7TXT = String.valueOf(adj7TXTBox.getText());
                String noun8TXT = String.valueOf(noun8TXTBox.getText());

                outPutTXT.setText("One day, I found a " + adj1TXT + " box in the " + adj2TXT + " attic. Inside, I discovered a " + adj3TXT + " " + noun4TXT + " covered in " + adj5TXT + " dust. As I opened it, a " + adj6TXT + " aroma filled the air, and I couldn't believe my eyes. The box contained a collection of " + adj7TXT + " " + noun8TXT + "!.");
                outPutLinear.setVisibility(View.VISIBLE);
                mainVerticalLayout.setVisibility(View.GONE);
                pic.setImageDrawable(getDrawable(R.drawable.attic));


            }
        });
        madLib3BTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String adj1TXT = String.valueOf(adj1TXTBox.getText());
                String adj2TXT = String.valueOf(adj2TXTBox.getText());
                String adj3TXT = String.valueOf(adj3TXTBox.getText());
                String noun4TXT = String.valueOf(noun4TXTBox.getText());
                String adj5TXT = String.valueOf(adj5TXTBox.getText());
                String adj6TXT = String.valueOf(adj6TXTBox.getText());
                String adj7TXT = String.valueOf(adj7TXTBox.getText());
                String adj8TXT = String.valueOf(noun8TXTBox.getText());

                outPutTXT.setText("Exploring the " + adj1TXT + " shipwreck on the " + adj2TXT + " shore was a thrilling adventure. Inside the ship, I discovered a " + adj3TXT + " " + noun4TXT + " covered in " + adj5TXT + " seaweed. As I inspected it, a  " + adj6TXT + " sound echoed through the dark corridors. I followed the sound and stumbled upon a " + adj7TXT + " " + adj8TXT + "!");
                outPutLinear.setVisibility(View.VISIBLE);
                mainVerticalLayout.setVisibility(View.GONE);
                pic.setImageDrawable(getDrawable(R.drawable.shiprec));



            }
        });

        randomBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Random randy = new Random();
                int random = randy.nextInt(3);
                if (random==0) {
                    madLib1BTN.callOnClick();
                }
                else if (random==1) {
                    madLib2BTN.callOnClick();
                }
                else if (random==2) {
                    madLib3BTN.callOnClick();
                }
                outPutLinear.setVisibility(View.VISIBLE);
                mainVerticalLayout.setVisibility(View.GONE);




            }
        });
        appearBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                outPutLinear.setVisibility(View.GONE);
                mainVerticalLayout.setVisibility(View.VISIBLE);

            }
        });

    }
}





