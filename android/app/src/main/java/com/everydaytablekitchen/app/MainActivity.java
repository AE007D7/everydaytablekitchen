package com.everydaytablekitchen.app;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends Activity {
    private static final String HOME = "https://www.everydaytablekitchen.com/";
    private WebView webView;

    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        webView = new WebView(this);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.getSettings().setDomStorageEnabled(true);
        webView.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri url = request.getUrl();
                String host = url.getHost();
                if ("https".equals(url.getScheme()) && ("www.everydaytablekitchen.com".equals(host) || "everydaytablekitchen.com".equals(host))) return false;
                try { startActivity(new Intent(Intent.ACTION_VIEW, url)); } catch (Exception ignored) { }
                return true;
            }
            @Override public void onReceivedError(WebView view, WebResourceRequest request, android.webkit.WebResourceError error) {
                if (request.isForMainFrame()) showOffline();
            }
        });
        setContentView(webView);
        webView.loadUrl(HOME);
    }

    private void showOffline() {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(48, 80, 48, 32);
        TextView message = new TextView(this);
        message.setText("Could not load recipes. Check your internet connection.");
        message.setTextSize(18);
        layout.addView(message);
        android.widget.Button retry = new android.widget.Button(this);
        retry.setText("Try again");
        retry.setOnClickListener(v -> { setContentView(webView); webView.loadUrl(HOME); });
        layout.addView(retry);
        setContentView(layout);
    }

    @Override public void onBackPressed() {
        if (webView.canGoBack()) webView.goBack(); else super.onBackPressed();
    }
    @Override protected void onDestroy() {
        webView.destroy();
        super.onDestroy();
    }
}
