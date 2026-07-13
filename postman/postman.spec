%global debug_package %{nil}

Name:           postman
Version:        12.19.0
Release:        %autorelease
Summary:        Postman API Platform

License:        Proprietary
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/postman
cp -a . %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -sf ../../opt/postman/Postman \
    %{buildroot}%{_bindir}/postman

install -Dpm0644 \
    %{SOURCE1} \
    %{buildroot}%{_datadir}/applications/postman.desktop

install -Dpm0644 \
    app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%check

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog