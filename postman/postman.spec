%global debug_package %{nil}

Name:           postman
Version:        12.16.1
Release:        %autorelease
Summary:        API platform for building and using APIs

License:        LicenseRef-Postman
URL:            https://www.postman.com/
Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
AutoReqProv:    no

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -n Postman

%install
install -d %{buildroot}/opt/postman
cp -a . %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -sf ../../opt/postman/Postman %{buildroot}%{_bindir}/postman

install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}

install -Dm0644 \
    app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog