package com.example.test123;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    int onTrayIncr = 0;
    int mainTrayIncr =0;
    int rollItemIncr = 0;
    int desertItemIncr = 0;
    int cookieItemIncr = 0 ;
    int soupItemIncr = 0;
    double total = 0.00;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView mealItemDisTXT = findViewById(R.id.textView3);
        TextView onTrayItemDisTXT = findViewById(R.id.textView4);
        TextView rollitemDisTxt = findViewById(R.id.textView5);
        TextView desertItemDisTxT = findViewById(R.id.textView6);
        TextView cookieItemDisTxT = findViewById(R.id.textView14);
        TextView totalPriceDisTXT = findViewById(R.id.textView2);
        TextView disChangeBackTXT = findViewById(R.id.textView7);
        EditText amountGivenTXT = findViewById(R.id.editTextText);



        Button mainAddBTN = findViewById(R.id.button13);
        Button mainDelBTN = findViewById(R.id.button14);
        Button onTrayAddBTN = findViewById(R.id.button24);
        Button onTrayDelBTN = findViewById(R.id.button25);
        Button rollItemAddBTN = findViewById(R.id.button28);
        Button rollItemDelBTN = findViewById(R.id.button29);
        Button desertItemAddBTN = findViewById(R.id.button26);
        Button desertItemDelBTN = findViewById(R.id.button27);
        Button cookieItemAddBTN = findViewById(R.id.button3);
        Button cookieItemDelBTN = findViewById(R.id.button4);
        Button expandOptionsBTN = findViewById(R.id.expandOptionsBTN);
        Button oneDollarAddBTN = findViewById(R.id.button8);
        Button fiveDollarAddBTN = findViewById(R.id.button9);
        Button tenDollarAddBTN = findViewById(R.id.button10);
        Button twentyDollarAddBTN = findViewById(R.id.button11);

        Button resetBTN = findViewById(R.id.button);
        Button calcBTN = findViewById(R.id.button6);
        LinearLayout outPutCostLayout = findViewById(R.id.outPutCostLayout);
        LinearLayout newOrderLayout = findViewById(R.id.newOrderLayout);
        LinearLayout inputLayout = findViewById(R.id.inputLayout);
        LinearLayout fieldDisplayLayout = findViewById(R.id.fieldDisplayLayout);
        LinearLayout buttonExraLayout = findViewById(R.id.buttonExraLayout);
        LinearLayout mainButtonLayout = findViewById(R.id.mainButtonLayout);


        outPutCostLayout.setVisibility((View.GONE));
        newOrderLayout.setVisibility((View.GONE));
        resetBTN.setVisibility((View.GONE));
        buttonExraLayout.setVisibility((View.GONE));
        expandOptionsBTN.setVisibility(View.VISIBLE);

        inputLayout.setVisibility((View.VISIBLE));
        fieldDisplayLayout.setVisibility((View.VISIBLE));
        mainButtonLayout.setVisibility((View.VISIBLE));
        expandOptionsBTN.setText("More Options");





        mainAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                mainTrayIncr++;
                //outputTXT.setText(entree);
                mealItemDisTXT.setText(Integer.toString(mainTrayIncr));
                total+=8;
                totalPriceDisTXT.setText("$"+Double.toString(total));


            }
        });
        mainDelBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (mainTrayIncr>0) {
                    mainTrayIncr--;
                    //outputTXT.setText(entree);
                    mealItemDisTXT.setText(Integer.toString(mainTrayIncr));
                    total -= 8;
                    totalPriceDisTXT.setText("$" + Double.toString(total));

                }
            }
        });
        onTrayAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){

                onTrayIncr++;
                //outputTXT.setText(entree);
                onTrayItemDisTXT.setText(Integer.toString(onTrayIncr));
                total += 3;
                totalPriceDisTXT.setText("$" + Double.toString(total));
            }

        });
        onTrayDelBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (onTrayIncr>0) {

                    onTrayIncr--;
                    //outputTXT.setText(entree);
                    onTrayItemDisTXT.setText(Integer.toString(onTrayIncr));
                    total -= 3;
                    totalPriceDisTXT.setText("$" + Double.toString(total));

                }
            }
        });
        rollItemAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                rollItemIncr++;
                //outputTXT.setText(entree);
                rollitemDisTxt.setText(Integer.toString(rollItemIncr));
                total+=.5;
                totalPriceDisTXT.setText("$"+Double.toString(total));


            }
        });
        rollItemDelBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (rollItemIncr>0) {

                    rollItemIncr--;
                    //outputTXT.setText(entree);
                    rollitemDisTxt.setText(Integer.toString(rollItemIncr));
                    total -= .5;
                    totalPriceDisTXT.setText("$" + Double.toString(total));

                }
            }
        });
        desertItemAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                desertItemIncr++;
                //outputTXT.setText(entree);
                desertItemDisTxT.setText(Integer.toString(desertItemIncr));
                total+=2;
                totalPriceDisTXT.setText("$"+Double.toString(total));


            }
        });
        desertItemDelBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (desertItemIncr>0) {

                    desertItemIncr--;
                    //outputTXT.setText(entree);
                    desertItemDisTxT.setText(Integer.toString(desertItemIncr));
                    total -= 2;
                    totalPriceDisTXT.setText("$" + Double.toString(total));

                }
            }
        });
        cookieItemAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){

                cookieItemIncr++;
                //outputTXT.setText(entree);
                cookieItemDisTxT.setText(Integer.toString(cookieItemIncr));
                total += 1;
                totalPriceDisTXT.setText("$" + Double.toString(total));


            }
        });
        cookieItemDelBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (cookieItemIncr>0) {

                    cookieItemIncr--;
                    //outputTXT.setText(entree);
                    cookieItemDisTxT.setText(Integer.toString(cookieItemIncr));
                    total -= 1;
                    totalPriceDisTXT.setText("$" + Double.toString(total));

                }
            }
        });
        oneDollarAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                try  {
                    double num1 = Double.parseDouble(amountGivenTXT.getText().toString());
                    num1++;
                    amountGivenTXT.setText(Double.toString(num1));
                }
                catch (Exception e){
                    double num1=0;
                    num1++;
                    amountGivenTXT.setText(Double.toString(num1));
                }


            }
        });
        fiveDollarAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                try  {
                    double num1 = Double.parseDouble(amountGivenTXT.getText().toString());
                    num1+=5;
                    amountGivenTXT.setText(Double.toString(num1));
                }
                catch (Exception e){
                    double num1=0;
                    num1+=5;
                    amountGivenTXT.setText(Double.toString(num1));
                }


            }
        });
        tenDollarAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                try  {
                    double num1 = Double.parseDouble(amountGivenTXT.getText().toString());
                    num1+=10;
                    amountGivenTXT.setText(Double.toString(num1));
                }
                catch (Exception e){
                    double num1=0;
                    num1+=10;
                    amountGivenTXT.setText(Double.toString(num1));
                }

            }
        });
        twentyDollarAddBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                try  {
                    double num1 = Double.parseDouble(amountGivenTXT.getText().toString());
                    num1+=20;
                    amountGivenTXT.setText(Double.toString(num1));
                }
                catch (Exception e){
                    double num1=0;
                    num1+=20;
                    amountGivenTXT.setText(Double.toString(num1));
                }


            }
        });



        expandOptionsBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (buttonExraLayout.getVisibility() == View.GONE) {
                    buttonExraLayout.setVisibility((View.VISIBLE));
                    expandOptionsBTN.setText("Collapse");
                    mainButtonLayout.setVisibility((View.GONE));

                }
                else{
                    buttonExraLayout.setVisibility((View.GONE));
                    expandOptionsBTN.setText("");
                    expandOptionsBTN.setText("More Options");
                    mainButtonLayout.setVisibility((View.VISIBLE));



                }



            }
        });
        resetBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                onTrayIncr = 0;
                total = 0.00;
                rollItemIncr = 0;
                soupItemIncr = 0;
                mainTrayIncr = 0;
                desertItemIncr = 0;
                cookieItemIncr = 0;
                totalPriceDisTXT.setText("$"+Double.toString(total));
                disChangeBackTXT.setText("$0.00");
                cookieItemDisTxT.setText(Integer.toString(cookieItemIncr));
                desertItemDisTxT.setText(Integer.toString(desertItemIncr));
                rollitemDisTxt.setText(Integer.toString(rollItemIncr));
                onTrayItemDisTXT.setText(Integer.toString(onTrayIncr));
                mealItemDisTXT.setText(Integer.toString(mainTrayIncr));
                mainButtonLayout.setVisibility((View.VISIBLE));
                amountGivenTXT.setText("");
                outPutCostLayout.setVisibility((View.GONE));
                newOrderLayout.setVisibility((View.GONE));
                resetBTN.setVisibility((View.GONE));

                inputLayout.setVisibility((View.VISIBLE));
                fieldDisplayLayout.setVisibility((View.VISIBLE));
                buttonExraLayout.setVisibility((View.GONE));
                expandOptionsBTN.setVisibility(View.VISIBLE);






            }
        });
        calcBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                //(!amountGivenTXT.equals(""))
                try  {
                    double num1 = Double.parseDouble(amountGivenTXT.getText().toString());
                    disChangeBackTXT.setText("$"+Double.toString(num1-total));
                }
                catch (Exception e){
                    disChangeBackTXT.setText("$"+Double.toString(-total));

                }

                //outputTXT.setText(entree);

                outPutCostLayout.setVisibility((View.VISIBLE));
                newOrderLayout.setVisibility((View.VISIBLE));
                resetBTN.setVisibility((View.VISIBLE));
                mainButtonLayout.setVisibility((View.GONE));

                inputLayout.setVisibility((View.VISIBLE));
                fieldDisplayLayout.setVisibility((View.VISIBLE));
                buttonExraLayout.setVisibility((View.GONE));
                amountGivenTXT.onEditorAction(EditorInfo.IME_ACTION_DONE);
                expandOptionsBTN.setVisibility(View.GONE);


            }
        });
    }

}