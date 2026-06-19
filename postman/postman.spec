%global debug_package %{nil}

Name:           postman
Version:        12.15.6
Release:        1%{?dist}
Summary:        API platform for building and using APIs

License:        Proprietary
URL:            https://www.postman.com/
Source0:        https://dl.pstmn.io/download/version/%{version}/linux64

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -c -n Postman

%build
cat > postman.desktop <<'EOF'
[Desktop Entry]
Name=Postman
Comment=API Platform for building and using APIs
Exec=postman %U
Terminal=false
Type=Application
Icon=postman
Categories=Development;Network;
StartupNotify=true
StartupWMClass=Postman
MimeType=x-scheme-handler/postman;
EOF

%install
install -dm755 %{buildroot}/opt/postman
cp -a Postman/. %{buildroot}/opt/postman/

install -dm755 %{buildroot}%{_bindir}
ln -s ../../opt/postman/Postman %{buildroot}%{_bindir}/postman

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    postman.desktop

install -dm755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
ln -s /opt/postman/app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog
